import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

def load_data(url):
    """
    Load the sales data from the URL
    """
    try:
        # Try to download the CSV data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Read the CSV content
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        print("Using a sample dataframe instead.")
        
        # Create a sample dataframe with similar structure if download fails
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December']
        
        sample_data = {
            'month_number': list(range(1, 13)),
            'month_name': months,
            'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
            'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
            'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 4580, 5200, 5300],
            'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 7800, 8200, 7500],
            'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
            'moisturizer': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
            'total_units': [21100, 18330, 22470, 22270, 20960, 20140, 20760, 25180, 23380, 20450, 22340, 21020],
            'total_profit': [29000, 21000, 26400, 31800, 35900, 30000, 32900, 39000, 37200, 29000, 35000, 33000]
        }
        
        return pd.DataFrame(sample_data)

def plot_total_profit(df):
    """
    Exercise 1: Read Total profit of all months and show it using a line plot
    """
    plt.figure(figsize=(12, 6))
    
    # Create x-axis values (month numbers)
    months = df['month_number']
    
    # Get the total profit for all months
    total_profit = df['total_profit']
    
    # Create the line plot
    plt.plot(months, total_profit, marker='o', linewidth=3, color='b')
    
    # Add labels and title
    plt.xlabel('Month Number')
    plt.ylabel('Total Profit')
    plt.title('Company Total Profit per Month')
    
    # Set the x-ticks to show all months
    plt.xticks(months)
    
    # Add gridlines
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add text labels for profit values
    for i, profit in enumerate(total_profit):
        plt.text(months[i], profit + 1000, f'${profit}', ha='center')
    
    plt.tight_layout()
    plt.savefig('total_profit.png')
    plt.show()
    
    print("Exercise 1: Total profit line plot has been created successfully.")

def plot_soap_facewash_subplots(df):
    """
    Exercise 2: Read data for Bathing soap and facewash of all months 
    and display it using the Subplot
    """
    plt.figure(figsize=(12, 8))
    
    # Create a 2x1 subplot (2 rows, 1 column)
    plt.subplot(2, 1, 1)  # First subplot (top)
    
    # Plot bathing soap data
    plt.plot(df['month_number'], df['bathingsoap'], marker='o', linewidth=3, 
             color='b', label='Bathing Soap')
    
    # Add labels and title for first subplot
    plt.xlabel('Month Number')
    plt.ylabel('Sales Units')
    plt.title('Monthly Bathing Soap Sales')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(df['month_number'])
    plt.legend()
    
    plt.subplot(2, 1, 2)  # Second subplot (bottom)
    
    # Plot facewash data
    plt.plot(df['month_number'], df['facewash'], marker='o', linewidth=3, 
             color='g', label='Face Wash')
    
    # Add labels and title for second subplot
    plt.xlabel('Month Number')
    plt.ylabel('Sales Units')
    plt.title('Monthly Face Wash Sales')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(df['month_number'])
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('soap_facewash_subplot.png')
    plt.show()
    
    print("Exercise 2: Bathing soap and facewash subplot has been created successfully.")

def main():
    # URL for the sales data
    url = "https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv"
    
    # Load the data
    df = load_data(url)
    
    # Display the first few rows
    print("Data Preview:")
    print(df.head())
    print("\n")
    
    # Exercise 1: Plot total profit
    plot_total_profit(df)
    
    # Exercise 2: Plot bathing soap and facewash as subplots
    plot_soap_facewash_subplots(df)

if __name__ == "__main__":
    main()