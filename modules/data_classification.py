import pandas as pd


def classify_columns(df):

    numerical = []
    categorical = []
    datetime = []
    boolean = []
    identifiers = []

    for column in df.columns:

        # Identify identifier columns
        if "id" in column.lower():
            identifiers.append(column)

        # Identify boolean columns
        elif pd.api.types.is_bool_dtype(df[column]):
            boolean.append(column)

        # Identify datetime columns
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            datetime.append(column)

        # Identify numerical columns
        elif pd.api.types.is_numeric_dtype(df[column]):
            numerical.append(column)

        # Identify categorical columns
        else:
            categorical.append(column)

    print("\n========== DATA TYPE CLASSIFICATION ==========")

    print("\nNumerical Columns:")
    print(numerical)

    print("\nCategorical Columns:")
    print(categorical)

    print("\nDate/Time Columns:")
    print(datetime)

    print("\nBoolean Columns:")
    print(boolean)

    print("\nIdentifier Columns:")
    print(identifiers)

    return {
        "numerical": numerical,
        "categorical": categorical,
        "datetime": datetime,
        "boolean": boolean,
        "identifiers": identifiers
    }   