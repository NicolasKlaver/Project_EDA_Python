{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94bbd5f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# First let's import the packages we will use in this project\n",
    "# You can do this all now or as you need them\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.mlab as mlab\n",
    "import matplotlib\n",
    "plt.style.use('ggplot')\n",
    "from matplotlib.pyplot import figure\n",
    "\n",
    "%matplotlib inline\n",
    "matplotlib.rcParams['figure.figsize'] = (12,8)\n",
    "\n",
    "pd.options.mode.chained_assignment = None\n",
    "\n",
    "\n",
    "\n",
    "# Now we need to read in the data\n",
    "df = pd.read_csv(r'C:\\Users\\alexf\\Downloads\\movies.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58db1fe9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Now let's take a look at the data\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66bdcab9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60a04fda",
   "metadata": {},
   "outputs": [],
   "source": [
    "# We need to see if we have any missing data\n",
    "# Let's loop through the data and see if there is anything missing\n",
    "\n",
    "for col in df.columns:\n",
    "    pct_missing = np.mean(df[col].isnull())\n",
    "    print('{} - {}%'.format(col, round(pct_missing*100)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "773477f6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04d9de2a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "625a1cf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data Types for our columns\n",
    "\n",
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f00f2cf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6983e18",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Are there any Outliers?\n",
    "\n",
    "df.boxplot(column=['gross'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ff4b466",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "baad2cea",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0a7136e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a4ad63f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Order our Data a little bit to see\n",
    "\n",
    "df.sort_values(by=['gross'], inplace=False, ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49289911",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "528eb0b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.regplot(x=\"gross\", y=\"budget\", data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4f1c797",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c97d118a",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.regplot(x=\"score\", y=\"gross\", data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ff33dca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6f7bbf2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Correlation Matrix between all numeric columns\n",
    "\n",
    "df.corr(method ='pearson')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1700d301",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.corr(method ='kendall')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03f5a310",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.corr(method ='spearman')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbf15833",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f810cd8",
   "metadata": {},
   "outputs": [],
   "source": [
    "correlation_matrix = df.corr()\n",
    "\n",
    "sns.heatmap(correlation_matrix, annot = True)\n",
    "\n",
    "plt.title(\"Correlation matrix for Numeric Features\")\n",
    "\n",
    "plt.xlabel(\"Movie features\")\n",
    "\n",
    "plt.ylabel(\"Movie features\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07ddae62",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ea47fc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using factorize - this assigns a random numeric value for each unique categorical value\n",
    "\n",
    "df.apply(lambda x: x.factorize()[0]).corr(method='pearson')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cd73e18",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0541e63e",
   "metadata": {},
   "outputs": [],
   "source": [
    "correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')\n",
    "\n",
    "sns.heatmap(correlation_matrix, annot = True)\n",
    "\n",
    "plt.title(\"Correlation matrix for Movies\")\n",
    "\n",
    "plt.xlabel(\"Movie features\")\n",
    "\n",
    "plt.ylabel(\"Movie features\")\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf420d87",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f0bd101",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()\n",
    "\n",
    "corr_pairs = correlation_mat.unstack()\n",
    "\n",
    "print(corr_pairs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6db16f22",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7052fa8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted_pairs = corr_pairs.sort_values(kind=\"quicksort\")\n",
    "\n",
    "print(sorted_pairs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11b1835d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ea7500b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# We can now take a look at the ones that have a high correlation (> 0.5)\n",
    "\n",
    "strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]\n",
    "\n",
    "print(strong_pairs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0270fe1e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a6337c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Looking at the top 15 compaies by gross revenue\n",
    "\n",
    "CompanyGrossSum = df.groupby('company')[[\"gross\"]].sum()\n",
    "\n",
    "CompanyGrossSumSorted = CompanyGrossSum.sort_values('gross', ascending = False)[:15]\n",
    "\n",
    "CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') \n",
    "\n",
    "CompanyGrossSumSorted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1563a49",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee3ebd7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Year'] = df['released'].astype(str).str[:4]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f23c6d26",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6f11702",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.groupby(['company', 'year'])[[\"gross\"]].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b632041",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e40f1e4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "CompanyGrossSum = df.groupby(['company', 'year'])[[\"gross\"]].sum()\n",
    "\n",
    "CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company','year'], ascending = False)[:15]\n",
    "\n",
    "CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') \n",
    "\n",
    "CompanyGrossSumSorted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f4492f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "CompanyGrossSum = df.groupby(['company'])[[\"gross\"]].sum()\n",
    "\n",
    "CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company'], ascending = False)[:15]\n",
    "\n",
    "CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64') \n",
    "\n",
    "CompanyGrossSumSorted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "585692d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.scatter(x=df['budget'], y=df['gross'], alpha=0.5)\n",
    "plt.title('Budget vs Gross Earnings')\n",
    "plt.xlabel('Gross Earnings')\n",
    "plt.ylabel('Budget for Film')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f2a6ec8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a75e0422",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_numerized = df\n",
    "\n",
    "\n",
    "for col_name in df_numerized.columns:\n",
    "    if(df_numerized[col_name].dtype == 'object'):\n",
    "        df_numerized[col_name]= df_numerized[col_name].astype('category')\n",
    "        df_numerized[col_name] = df_numerized[col_name].cat.codes\n",
    "        \n",
    "df_numerized"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78244f70",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_numerized.corr(method='pearson')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb21939f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc42a05d",
   "metadata": {},
   "outputs": [],
   "source": [
    "correlation_matrix = df_numerized.corr(method='pearson')\n",
    "\n",
    "sns.heatmap(correlation_matrix, annot = True)\n",
    "\n",
    "plt.title(\"Correlation matrix for Movies\")\n",
    "\n",
    "plt.xlabel(\"Movie features\")\n",
    "\n",
    "plt.ylabel(\"Movie features\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ec221db",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6572c88d",
   "metadata": {},
   "outputs": [],
   "source": [
    "for col_name in df.columns:\n",
    "    if(df[col_name].dtype == 'object'):\n",
    "        df[col_name]= df[col_name].astype('category')\n",
    "        df[col_name] = df[col_name].cat.codes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71294bc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb13f920",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36eb2eb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.swarmplot(x=\"rating\", y=\"gross\", data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bbc0465",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "sns.stripplot(x=\"rating\", y=\"gross\", data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b410152",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c4742e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
