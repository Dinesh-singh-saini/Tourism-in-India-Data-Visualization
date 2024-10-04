import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'India-Tourism-Statistics-2022-TABLE-2.1.2.csv'
tourism_data = pd.read_csv(file_path)


# Function to plot tourist arrivals
def plot_tourist_arrivals():
    plt.figure(figsize=(10, 6))
    plt.plot(tourism_data['Months'], tourism_data['2019'], marker='o', label='2019')
    plt.plot(tourism_data['Months'], tourism_data['2020'], marker='o', label='2020')
    plt.plot(tourism_data['Months'], tourism_data['2021'], marker='o', label='2021')
    plt.title('Tourist Arrivals in India (2019-2021)', fontsize=16)
    plt.xlabel('Months', fontsize=12)
    plt.ylabel('Number of Tourists', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Function to plot growth percentages
def plot_growth_percentages():
    plt.figure(figsize=(10, 6))
    plt.plot(tourism_data['Months'], tourism_data['Growth 2020/19 (%)'], marker='o', label='Growth 2020/19 (%)')
    plt.plot(tourism_data['Months'], tourism_data['Growth 2021/20 (%)'], marker='o', label='Growth 2021/20 (%)')
    plt.title('Growth Percentages in Tourist Arrivals (2019-2021)', fontsize=16)
    plt.xlabel('Months', fontsize=12)
    plt.ylabel('Growth (%)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Function to plot total tourists comparison
def plot_total_comparison():
    totals = [tourism_data['2019'].sum(), tourism_data['2020'].sum(), tourism_data['2021'].sum()]
    years = ['2019', '2020', '2021']

    plt.figure(figsize=(8, 5))
    plt.bar(years, totals, color=['blue', 'orange', 'green'])
    plt.title('Total Tourists Comparison (2019-2021)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Tourists', fontsize=12)
    plt.tight_layout()
    plt.show()


# Menu function
def display_menu():
    print("Tourism Data Visualization Menu")
    print("1. Plot Tourist Arrivals (2019-2021)")
    print("2. Plot Growth Percentages (2020 vs 2019, 2021 vs 2020)")
    print("3. Compare Total Tourists (2019, 2020, 2021)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    return choice


# Main program loop
while True:
    user_choice = display_menu()

    if user_choice == '1':
        plot_tourist_arrivals()
    elif user_choice == '2':
        plot_growth_percentages()
    elif user_choice == '3':
        plot_total_comparison()
    elif user_choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
