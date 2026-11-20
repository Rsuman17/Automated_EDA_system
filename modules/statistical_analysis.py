import pandas as pd
import numpy as np

def analyze_statistics(df):
    numeric_columns=df.select_dtypes(include="number").columns
    numeric_columns= [
        col for col in numeric_columns
        if "id" not in col.lower()
            ]
    
    print("\nNumeric Columns:")
    print(list(numeric_columns))

# Central tendancy analysis

    central_tendency ={}
    for col in numeric_columns:
        mean_value=df[col].mean()
        median_value=df[col].median()

        mode_value=df[col].mode().tolist()

        central_tendency[col]={
            "Mean":mean_value,
            "Median":median_value,
            "Mode":mode_value
        }

    print("\n Central Tendency Results:")
    print(pd.DataFrame(central_tendency).T)
    
#Range & Quartile Analysis

    distribution={}
    for col in numeric_columns:
        minimum=df[col].min()
        maximum=df[col].max()

        q1=df[col].quantile(0.25)
        q2=df[col].quantile(0.50)
        q3=df[col].quantile(0.75)
        iqr=q3-q1

        distribution[col]={
            "Minimum":minimum,
            "Maximum":maximum,
            "Q1":q1,
            "Q2":q2,
            "Q":q3,
            "IQR":iqr
        }
        print("\nQuartile and Range Analysis:")
        print(pd.DataFrame(distribution).T)

# Skewness Analysis: Near 0, Positive Skewed, negative skewed
    skewness={}
    for col in numeric_columns:
        skew_value = df[col].skew()
        skewness[col]=skew_value
    print("\nSkewness:")
    print(pd.Series(skewness,name="Skewness"))


# correlation Matrix
    correlation_matrix=df[numeric_columns].corr()
    print("\n Correlation Matrix:")
    print(correlation_matrix)

# Covarience Analysis: Ranges -1 to +1
    covariance_matrix=df[numeric_columns].cov()
    print("\n Covarience Matrix:")
    print(covariance_matrix)

    