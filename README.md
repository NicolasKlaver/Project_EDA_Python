# Project EDA Python

In this project I make a Introductory analysis of the Movies dataset. 

The first approach is to do Data Cleaning and then see the correlation between the columns, particulary we are gonna to analyse the Gross column.
And finally leave some topics that may be interesting to review in the future and make a more complete project


#### Libraries used: 
- pandas, numpy, matplotlib and seaborn.


#### Skills used: 
- Data Cleaning and Data Visualization.




###### Link to the kaggle dataset: [Click Here](https://www.kaggle.com/datasets/danielgrijalvas/movies)


#### Files
- movies.ipynb: contains all the project




## Let's review some aspect of the project




### First View of the Data
![](https://github.com/NicolasKlaver/Project_EDA_Python/blob/main/img/first_data.png)



### Describe
![](https://github.com/NicolasKlaver/Project_EDA_Python/blob/main/img/describe_data.png)
##### Notes:
- The studied time lapse goes from 1980 to 2020.
- The max score is 9.3.



### Data Types
![](https://github.com/NicolasKlaver/Project_EDA_Python/blob/main/img/data_types.png)
##### Notes:
- Numerical columns: Budget, Gross, Runtime, Score, Votes and RunTime
- Categorical columns: Company, Country, Director, Genre, Name, Rating, Star and Writer.
- Date columns: Released and Year.



### Correlation Matrix
![](https://github.com/NicolasKlaver/Project_EDA_Python/blob/main/img/heatmap_correlation.png)
##### Notes:
- Gross has a high correlation with Budget and Votes



### Scatter Plot between Gross vs Budget
![](https://github.com/NicolasKlaver/Project_EDA_Python/blob/main/img/scatter_buget_gross.jpg)
##### Notes:
- We see a positive correlation between Budget and Gross



