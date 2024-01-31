#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:50:51 2024

@author: grantoctober
"""

# import pandas as pd

# df = pd.read_csv("data_02/country_data_index.csv")

# import pandas as pd

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)


# df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")


# file = pd.read_excel("data_02/residentdoctors.xlsx")


# df = pd.read_json("data_02/student_data.json")

# df = pd.read_csv("data_02/country_data_index.csv",index_col=0)

# column_names = ["duration", "pulse", "max_pulse", "calories"]

# df = pd.read_csv("data_02/patient_data.csv", header=None, names=column_names)

# df = pd.read_csv("data_02/Geospatial Data.txt")

# df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

# # Step 1: Extract the lower end of the age range (digits only)
# df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')

# # Step 2: Convert the new column to float
# df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)


# df = pd.read_csv("data_02/time_series_data.csv")

# # Convert the 'Date' column to datetime
# df['Date'] = pd.to_datetime(df['Date'])

# df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# # Split the 'Date' column into separate columns for year, month, and day
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day



# import pandas as pd

# df = pd.read_csv('data_02/patient_data_dates.csv')

# # Allows you to see all rows
# pd.set_option('display.max_rows',None)

# print(df)


# df.drop(['Index'],inplace=True,axis=1)

# x = df["Calories"].mean()

# df['Date'] = pd.to_datetime(df['Date'])

# df.dropna(inplace = True)
# df = df.reset_index(drop=True)

# df["Calories"].fillna(x, inplace = True) 

# df.loc[7, 'Duration'] = 45:
    
# df.drop_duplicates(inplace = True)


# import pandas as pd

# df = pd.read_csv('data_02/patient_data_dates.csv')

# pd.set_option('display.max_rows',None)

# print(df)

# # Drop Index Column:

# df.drop(['Index'],inplace=True,axis=1)

# print(df)

# # Fill NaNs or empty fields in Calorie Column

# x = df["Calories"].mean()

# df["Calories"].fillna(x, inplace = True)

# print(df)

# # Convert Wrong Date Format in Date Column

# df['Date'] = pd.to_datetime(df['Date'])

# # Drop NaT field in Date Column

# df.dropna(subset=['Date'], inplace = True)

# print(df)

# # Remove any rows that have NaNs or empty fields
# # Here only the row 1 for the MaxPulse column as the rest have been resolved
# df.dropna(inplace = True)

# # Reset index
# df = df.reset_index(drop=True)

# print(df)

# # Remove duplicates found in line 10 and 11
# df.drop_duplicates(inplace = True)

# df = df.reset_index(drop=True)

# print(df)


grouped = df.groupby('class')

# Calculate mean, sum, and count for the squared values
mean_squared_values = grouped['sepal_length_sq'].mean()
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

# Display the results
print("Mean of Sepal Length Squared:")
print(mean_squared_values)

print("\nSum of Sepal Length Squared:")
print(sum_squared_values)

print("\nCount of Sepal Length Squared:")
print(count_squared_values)


import pandas as pd

# Read the CSV files into dataframes
df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

# Concatenate the dataframes
df = pd.concat([df1, df2], ignore_index=True)


df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')

## inner join
df_merge = pd.merge(df1,df2,on='id')

df_merge = pd.merge(df1, df2, on='id', how='outer')

# Filtering data
print(df[df['age'] > 30])


# Filter data for females (class == 'Iris-versicolor')
iris_versicolor = df[df['class'] == 'Iris-versicolor']

# Calculate the average iris_versicolor_sep_length
avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean()

df['class'] = df['class'].str.replace('Iris-', '')

# Apply the square to sepal length using a lambda function
df['sepal_length_sq'] = df['sepal_length'].apply(lambda x: x**2)


#CSV
df.to_csv("data_02/output/iris_data_cleaned.csv")

df.to_csv("data_02/output/iris_data_cleaned.csv", index=False)

#Excel
df.to_excel("data_02/output/iris_data_cleaned.xlsx", index=False, sheet_name='Sheet1')

#JSON
df.to_json("data_02/output/iris_data_cleaned.json", orient='records')

