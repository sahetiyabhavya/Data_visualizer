import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs

class Data_Analyzer():
    def __init__(self):
        self.data = None

    def load_data(self):
        try:
            path = input("Enter Dataset Path (e.g. data/Report_sales.csv): ").strip()
            self.data = pd.read_csv(path)
            print("Dataset Loaded Successfully!")
            return self.data
        except :
            print("Invalid file Name")
            return

    def explore_data(self):

        if self.data is None :
            print("Please load the Dataset First")
            return
        elif self.data.empty:
            print("Dataset is Empty!")
            return

        print("=== Explore Data ===")
        print("1. Display the First 5 Rows")
        print("2. Display the Last 5 Rows")
        print("3. Display Column Names")
        print("4. Display Data Types")
        print("5. Display Basic Information")

        try:
            choice = int(input("Enter your Choice: "))

            if choice == 1  :
                print(self.data.head())

            elif choice == 2 :
                print(self.data.tail())

            elif choice == 3 :
                print(self.data.columns)

            elif choice == 4 :
                print(self.data.dtypes)

            elif choice == 5 :
                print(self.data.info())

            else :
                print("Enter Valid Choice!")

        except :
            print("Something Went Wrong!")

    def performance_data(self):
        if self.data is None:
            print("Please load Dataset First!")
            return

        print("=== DataFrame Operations ===")
        print("1. Sum of Sales")
        print("2. Top 5 Products with Highest Sales")
        print("3. Top 5 Products with Lowest Sales")
        print("4. Region with Highest Sales")
        print("5. Total Quantity Sold by Each Product")

        try:
            choice = int(input("Enter your Choice: "))

            if choice == 1 :
                print("Total sales:", self.data["Sales"].sum())

            elif choice == 2 :
                print("Higest sales :",self.data['Sales'].nlargest(5))

            elif choice == 3 :
                print("Lowest sales :",self.data['Sales'].nsmallest(5))

            elif choice == 4:
                sales = self.data.groupby("Region")["Sales"].sum()
                print("Region with Highest Sales:", sales.idxmax())

            elif choice == 5:
                print(self.data.groupby("Product")["Quantity"].sum())

            else:
                print("Enter Valid Choice")
        except :
            print("Something Went Wrong!")

    def missing_value(self):
            
        if self.data is None:
            print("Please load Dataset First!")
            return

        print("=== Handle Missing Data ===")
        print("1. Display Rows with Missing Values")
        print("2. Fill Missing Values with Mean")
        print("3. Drop Rows with Missing Values")
        print("4. Replace Missing Values with a Specific Value")

        try:
            choice = int(input("Enter your Choice: "))

            if choice == 1 :
                print('=== Before ===')
                value = self.data.isnull().sum()
                print(value)

            elif choice == 2 :
                self.data.fillna(self.data.mean(numeric_only=True))
                print(self.data.isnull().sum())

            elif choice == 3 :
                print('=== Before ===')
                self.data.isnull().sum()
                self.data.dropna(inplace=True)
                print("=== After ===")
                print(self.data.isnull().sum())
                print("Rows with Missing Values Removed!")

            elif choice == 4 :
                value = input("Enter Value to Replace Missing Values: ")
                self.data.fillna(value, inplace=True)
                print("Missing Values Replaced Successfully!")
                print(self.data.isnull().sum())

            else:
                print("Enter Valide Choice!")

        except :
            print("Something Went Wrong!")
 
    def statistics_data(self):
        if self.data is None:
            print("Please load the Dataset First!")
            return
        print(self.data.describe().columns)
        column = input("Enter Column Name: ")

        if column not in self.data.columns:
            print("Column Not Found!")
            return
 
        print("1. Minimum")
        print("2. Maximum")
        print("3. Average")
        print("4. Median")
        print("5. Standard Deviation")

        try:
            choice = int(input("Enter your Choice: "))
        except ValueError:
            print("Enter Valid Choice!")
            return

        if choice == 1:
            print("Minimum: ", self.data.min(numeric_only=True))
        elif choice == 2:
            print("Maximum: ", self.data.max(numeric_only=True))
        elif choice == 3:
            print("Average: ", self.data.mean(numeric_only=True))
        elif choice == 4:
            print("Median: ", self.data.median(numeric_only=True))
        elif choice == 5:
            print("Standard Deviation: ", self.data.std(numeric_only=True))
        else:
            print("Enter Valid Choice!")

    def data_visualization(self):
        print("\n======== DATA VISUALIZATION ========")
        print("Bar Plot")
        print("Line Plot")
        print("Scatter Plot")
        print("Pie Chart")
        print("Histogram")
        print("Area Plot")

        plot_type = input("\nChoose Plot: ").lower().strip()
        print("\nAvailable Columns:")
        print(self.data.columns.tolist())
        
        try:
            if plot_type in ["Bar", "line", "scatter", "area"]:
                x = input("Enter X-axis column: ").strip()
                y = input("Enter Y-axis column: ").strip()

                if x not in self.data.columns or y not in self.data.columns:
                    print("Column Not Found!")
                    return
                self.fig, x = plt.subplots(figsize=(10, 5))

                if plot_type == "Bar":
                    sbs.barplot(data=self.data, x=x, y=y,errorbar=None)
                elif plot_type == "line":
                    sbs.lineplot(data=self.data, x=x, y=y, marker="o")
                elif plot_type == "scatter":
                    sbs.scatterplot(data=self.data, x=x, y=y)
                elif plot_type == "area":
 
                    sbs.lineplot(data=self.data, x=x, y=y, marker="o")
                    plt.xticks(rotation=45)

                plt.xlabel(x)
                plt.ylabel(y)
                plt.title(plot_type.capitalize() + "Plot")
                plt.grid(alpha=0.3)

            elif plot_type == "Pie":
 
                x = input("Enter Category Column: ").strip()
                y = input("Enter Value Column: ").strip()

                if x not in self.data.columns or y not in self.data.columns:
                    print("Column Not Found!")
                    return

                data = self.data.groupby(x)[y].sum()

                plt.figure(figsize=(8, 6))
                plt.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
                plt.title(x + " Wise " + y + " Analysis")
                        
            elif plot_type == "Histogram":
                column = input("Enter Column Name: ").strip()

                if column not in self.data.columns:
                    print("Column Not Found!")
                    return

                plt.figure(figsize=(10, 5))
                sbs.histplot(data=self.data, x=column, bins=10)
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.title("Histogram")
                plt.grid(alpha=0.3)

            else:
                print("Invalid plot Type!")
                return

            plt.tight_layout()
            plt.legend(loc="Upper right")
            plt.show() 
        except:
                print("something Went Wrong, Please try again")

    def save_visualization(self):
        if not hasattr(self, "fig") or self.fig is None:
            print("Please Generate a Graph First!")
            return

        file_name = input("Enter File Name: ").strip()

        if not file_name:
            print("File Name cannot be Empty!")
            return

        try:
            self.fig.savefig(f"plot/{file_name}.png", dpi=300, bbox_inches="tight")
            print(f"Graph Saved Successfully: plot/{file_name}.png")

        except :
            print("Unable to Save Graph")
 
 
    def main_menu(self):
        print()
        print("="*8, "Data Analysis & Visualization Program", "=" *8)
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 55)

    def start_Programe(self):
        while True:
            self.main_menu()

            try:
                choice = int(input("Enter your Choice: "))
            except :
                print("Enter Valid Choice!")
                continue

            print()
            if choice == 1:
                self.load_data()

            elif choice == 2:
                self.explore_data()

            elif choice == 3:
                self.performance_data()

            elif choice == 4:
                self.missing_value()

            elif choice == 5:
                self.statistics_data()

            elif choice == 6:
                self.data_visualization()

            elif choice == 7:
                self.save_visualization()

            elif choice == 8:
                print("Exiting the Program")
                
                break
            else:
                print("Invalid choicz!")


obj = Data_Analyzer()
obj.start_Programe()