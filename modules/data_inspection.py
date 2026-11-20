def inspect_dataset(df):
    print("1. Dataset Shape:", df.shape)
    print("\n2. Column Names:")
    print(df.columns.tolist())
    print("\n3. Data Types:")
    print(df.dtypes)
    print("\n4. Missing Values:")
    print(df.isnull().sum())
    print("\n5. Duplicate Records:")
    print(df.duplicated().sum())








    