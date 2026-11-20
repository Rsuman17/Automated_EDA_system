import pandas as pd

# Null values:
def check_missing_values(df):
    missing = df.isnull().sum()
    missing_percentage = (missing / len(df) * 100).round(2)
    
    report = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_percentage})
    print("Missing Values Report:")
    print(report)
    return report
# Duplicates:
def check_duplicates(df):
    count = df.duplicated().sum()
    print("Total Duplicates Records:", count)
    return count

def check_text_inconsistency(df):
    text_columns = df.select_dtypes(include=["object", "string", "category"]).columns
    
    for column in text_columns:
        # Remove empty values and make sure every value is text.
        raw_text = df[column].dropna().astype(str)
        
        # Count rows that change when leading/trailing spaces are removed.
        trimmed_text = raw_text.str.strip()
        extra_spaces_count = (raw_text != trimmed_text).sum()
        
        # Check if converting to lowercase reduces the number of unique values
        lowercase_text = trimmed_text.str.lower()
        has_case_mismatch = lowercase_text.nunique() < raw_text.nunique()
        
        # Only print if we found an issue
        if extra_spaces_count > 0 or has_case_mismatch:
            print(f"\nColumn: {column}")
            print(f"Values with extra spaces: {extra_spaces_count}")
            print(f"Possible capitalization inconsistency: {has_case_mismatch}")

def check_outliers(df):
    numerical_columns = df.select_dtypes(include='number').columns
    numerical_columns = []
    for col in numerical_columns:
        if "id" not in col.lower():
            numerical_columns.append(col)
    
    outlier_report = {}
    
    for col in numerical_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        
        outlier_report[col] = len(outliers)
        print(f"{col}: {len(outliers)} potential outliers")
        
    return outlier_report


 # 5. DATA QUALITY SUGGESTIONS

def analyze_data_quality(df):
    print("\n5. DATA QUALITY SUGGESTIONS")
    
    missing_report = check_missing_values(df)
    if missing_report['Missing Values'].sum() > 0:
        print("- Review missing values and decide how to handle them.")
    else:
        print("- No missing values detected.")
        
    duplicate_count = check_duplicates(df)
    if duplicate_count > 0:
        print("- Review duplicate records before removing them.")
    else:
        print("- No duplicate records detected.")
        
    print("- Investigate potential outliers before modifying data.")
    print("- Review inconsistent categorical values.")
    print("\n========== ANALYSIS COMPLETED ==========")


