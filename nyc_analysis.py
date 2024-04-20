import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("schools.csv")

def check_df(dataframe):
    print("################################################### HEAD ##########################################################################")
    print(df.head())
    print("################################################### DESCRIBE ######################################################################")
    print(df.describe().T)
    print("################################################### INFO ######################################################################")
    print(df.info())
    print("################################################### DESCRIBE ######################################################################")
    print(df.describe())
    print("################################################### SHAPE ######################################################################")
    print(df.shape)
    print("################################################### DTYPES ######################################################################")
    print(df.dtypes)
    print("################################################### NAs ######################################################################")
    print(df.isnull().sum())

#check_df(df)

# Step 1: Finding schools with the best math scores

best_math_schools = df[df["average_math"] > 800 * 0.80][["school_name", "average_math"]].sort_values(by = "average_math", ascending = False).head(10)
print(best_math_schools)

# Step 2: Identify the top 10 performing schools


df["total_SAT"] = df["average_math"] + df["average_reading"] + df["average_writing"]
top_10_schools = df[["school_name","total_SAT"]].sort_values(by = "total_SAT", ascending = False).head(10)
print(top_10_schools)


# Step 3: Locating the NYC borough with the largest standard deviation in SAT performance

df_boroughs = df.groupby("borough")["total_SAT"].agg(["count", "mean","std"]).round(2)
df_boroughs.rename(columns = {"count": "num_schools", "mean" : "average_SAT", "std" : "std_SAT"}, inplace = True)
largest_std = df_boroughs["std_SAT"].max()
largest_std_borough = df_boroughs[df_boroughs["std_SAT"] == largest_std]
largest_std_borough.reset_index(inplace = True)
print(largest_std_borough)

"""
Comments:

    Manhattan has the largest standart deviation in SAT performance in NYC.
    Stuyvesant High School has the highest average_math score in SAT in NYC
    Stuyvesant High School also has the highest total SAT performance in NYC.
"""
