import pandas as pd
from modules.data_inspection import inspect_dataset
from modules.data_classification import classify_columns
from modules.data_quality import check_missing_values,check_duplicates,check_text_inconsistency,check_outliers
from modules.statistical_analysis import analyze_statistics
from modules.data_visualization import run_visualization

# Load the dataset
df = pd.read_csv("data/shopping_trends_updated.csv")

# Display first 5 records
print(df.head())


# Inspect the dataset
inspect_dataset(df)

# Classify columns by data type
classify_columns(df)

# Analyze Data quality
check_missing_values(df)
check_duplicates(df)
check_text_inconsistency(df)
check_outliers(df)
analyze_statistics(df)
run_visualization(df)

