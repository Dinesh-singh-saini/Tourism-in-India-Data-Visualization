# Tourism in India Data Visualization

This project visualizes tourism statistics in India for the years 2019, 2020, and 2021. The goal is to understand trends
and growth in tourist arrivals, especially the impact of the COVID-19 pandemic on tourism. The project provides a
menu-based interface to explore different visualizations.

## Features

1. **Tourist Arrivals (2019-2021)**: A line plot showing the number of tourist arrivals across the months for 2019,
   2020, and 2021.
2. **Growth Percentages**: A line plot that compares the percentage growth in tourist numbers from 2019 to 2020, and
   2020 to 2021.
3. **Total Tourists Comparison**: A bar chart that compares the total number of tourists for the three years.

## Dataset

The dataset used contains monthly tourist statistics for 2019, 2020, and 2021, along with percentage growth rates
between consecutive years.

### Sample Data:

| Month    | 2019   | 2020   | 2021   | Growth 2020/19 (%) | Growth 2021/20 (%) |
|----------|--------|--------|--------|--------------------|--------------------|
| January  | 440907 | 611702 | 486338 | 38.74              | -20.49             |
| February | 402203 | 495109 | 431118 | 23.10              | -12.92             |
| ...      | ...    | ...    | ...    | ...                | ...                |

## Technologies

- **Python**: Core programming language.
- **Pandas**: Used for data manipulation.
- **Matplotlib**: Used for creating visualizations.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dinesh-singh-saini/Tourism-in-India-Data-Visualization.git

2. **Navigate to the project directory**:
    ```bash
    cd Tourism-in-India-Data-Visualization

3. **Install the required packages**:
    ```bash
   pip install pandas matplotlib
4. **Run the script**:
    ```bash
    python main.py
    ```

## Usage

After running the script, a menu will be displayed in the terminal:

```Tourism Data Visualization Menu
1. Plot Tourist Arrivals (2019-2021)
2. Plot Growth Percentages (2020 vs 2019, 2021 vs 2020)
3. Compare Total Tourists (2019, 2020, 2021)
4. Exit
Enter your choice: 
```

Enter the number corresponding to the visualization you want to see and press Enter. The visualization will be displayed
in a new window.

## Visualizations

1. **Tourist Arrivals (2019-2021)**:
   Shows the number of tourists visiting India each month in 2019, 2020, and 2021.
2. **Growth Percentages (2020 vs 2019, 2021 vs 2020)**:
   Visualizes the growth rates in tourist arrivals between consecutive years, showing the impact of the pandemic.
3. **Total Tourists Comparison**:
   Compares the total number of tourists for the years 2019, 2020, and 2021 using a bar chart.
4. **Exit**:
   Closes the program.

## License
This project is licensed under the [Apache License](LICENSE).