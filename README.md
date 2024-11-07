# Tourism Data Visualization

This project provides an interactive menu-driven system to visualize tourism data of Indian states over time. The program uses `pandas` for data manipulation and `matplotlib` for visualizations.

## Features
- **Total Tourists by State**: Displays a bar chart of the total number of tourists visiting each state.
- **Monthly Tourist Trends for a State**: Allows the user to input a state name and see the tourist trends over time in that state.
- **Top 5 States by Total Tourists**: Displays the top 5 states with the highest number of tourists.
- **Growth Percentage by State**: Visualizes the growth percentage of tourists for each state.

## Requirements
To run this project, you'll need to have the following Python libraries installed:

- `pandas`
- `matplotlib`

You can install these dependencies using the following command:

```bash
pip install pandas matplotlib
pip install pandas matplotlib
```   
## Getting Started
* Clone or download the project.
* Make sure you have the ``tourism_data_indian_states.csv`` file containing the tourism data in the same directory.
* Run the ```main.py``` script.

## How to Use
1. After running the script, you'll be presented with a menu of options. 
2. Select an option by entering a number (1-5).
3. For the "Monthly Tourist Trends for a State" option, you'll be asked to input a state name. 
4. Visualizations will be displayed for the selected option.

## Example Menu
--- Tourism Data Visualization Menu ---
1. Total Tourists by State
2. Monthly Tourist Trends for a State
3. Top 5 States by Total Tourists
4. Growth Percentage by State
5. Exit

## Data
The dataset tourism_data_indian_states.csv should include columns such as:

* State: The name of the state.
* Month: The month of the data. 
* Year: The year of the data. 
* Total_Tourists: The total number of tourists for the respective state, month, and year. 
* Growth_Percentage: The growth percentage of tourists for the state (optional column). 

## Example Output
* Total Tourists by State: A bar chart of tourists across states. 
* Monthly Tourist Trends for a State: A line chart displaying the trend for a specific state. 
* Top 5 States by Total Tourists: A bar chart showing the top 5 states with the highest tourist numbers. 
* Growth Percentage by State: A bar chart representing the growth percentage for each state.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.