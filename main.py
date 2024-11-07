import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('tourism_data_indian_states.csv')

data['Date'] = pd.to_datetime(data['Month'] + ' ' + data['Year'].astype(str))


def tourism_visualization_menu():
    while True:
        print("\n--- Tourism Data Visualization Menu ---")
        print("1. Total Tourists by State")
        print("2. Monthly Tourist Trends for a State")
        print("3. Top 5 States by Total Tourists")
        print("4. Growth Percentage by State")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            total_tourists_by_state()
        elif choice == '2':
            monthly_tourist_trends()
        elif choice == '3':
            top_5_states_by_tourists()
        elif choice == '4':
            growth_percentage_by_state()
        elif choice == '5':
            print("Exiting the menu. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


def total_tourists_by_state():
    plt.figure(figsize=(12, 6))
    state_totals = data.groupby('State')['Total_Tourists'].sum().sort_values()
    state_totals.plot(kind='bar', color='skyblue')
    plt.title("Total Tourists by State")
    plt.xlabel("Total Tourists")
    plt.ylabel("State")
    plt.tight_layout()
    plt.show()


def monthly_tourist_trends():
    state_name = input("Enter the state name to view monthly trends: ")
    state_data = data[data['State'] == state_name]
    if state_data.empty:
        print(f"No data found for the state '{state_name}'.")
        return
    plt.figure(figsize=(10, 5))
    plt.plot(state_data['Date'], state_data['Total_Tourists'], marker='o', linestyle='-', color='green')
    plt.title(f"Monthly Tourist Trends in {state_name}")
    plt.xlabel("Date")
    plt.ylabel("Total Tourists")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def top_5_states_by_tourists():
    plt.figure(figsize=(8, 5))
    top_5_states = data.groupby('State')['Total_Tourists'].sum().nlargest(5)
    top_5_states.plot(kind='bar', color='coral')
    plt.title("Top 5 States by Total Tourists")
    plt.xlabel("State")
    plt.ylabel("Total Tourists")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def growth_percentage_by_state():
    plt.figure(figsize=(12, 6))
    plt.bar(data['State'], data['Growth_Percentage'])
    plt.title("Growth Percentage by State")
    plt.xlabel("State")
    plt.ylabel("Growth Percentage")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

tourism_visualization_menu()