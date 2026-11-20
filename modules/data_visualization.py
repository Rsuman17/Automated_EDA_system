import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def select_column(df):
    numeric_columns=df.select_dtypes(include="number").columns.tolist()
    numeric_columns=[
        col for col in numeric_columns
        if "id" not in col.lower()
    ]
    print("\n Available Numarical Columns:")

    for col in numeric_columns:
        print(col)

    selected_column=input("Enter a column name:")

    if selected_column not in numeric_columns:
        print("Invalid column name!")
        return None

    return selected_column 
   
# Choose Visualization

def choose_visualization():
    print("\nAvailable Visualizations:")
    print("1.Histogram")
    print("2.Boxplot")
    print("3.KDE plot")
    print("4.Scatter plot")
    print("5.Co-relation Heatmap")

    choice=input("\nChoose Visualization (1-5):")
    return choice

# Generate visualization

def generate_visualization(df, column, choice,y_column=None):
    plt.figure(figsize=(8, 5))
    if choice == "1":

        sns.histplot(data=df, x=column,bins=50, kde=True)
        plt.title(f"Histogram of {column}")

    elif choice == "2":

        sns.boxplot(data=df, x=column)
        plt.title(f"Boxplot of {column}")

    elif choice == "3":

        sns.kdeplot(data=df, x=column)
        plt.title(f"KDE Plot of {column}")

    elif choice =="4":

        sns.scatterplot(data=df,x=column,y=y_column)
        plt.title(f"{column}vs{y_column}")

    elif choice == "5":

        sns.heatmap(data=df.corr(),annot=True,cmap="coolwarm",fmt=".2f",center=0
    )

        plt.title("Correlation Heatmap")

    else:
        print("Invalid visualization choice!")
        plt.close()
        return

    plt.tight_layout()
    plt.show()

def run_visualization(df):
    choice = choose_visualization()
    column = select_column(df)

    if choice =="5":
        generate_visualization(df,None,choice)
        return

    column=select_column(df)
    if column is None:
        return
    y_column = None

    if choice == "4":
        y_column = select_column(df)
        if y_column is None or column == y_column:
            print("Select two different valid columns!")
            return

    generate_visualization(df, column, choice, y_column)
