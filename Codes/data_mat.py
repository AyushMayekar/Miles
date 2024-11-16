import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# CSV file path
CSV_FILE = "temperature_data.csv"

def plot_temperature_data(csv_file):
    """
    Reads temperature data from a CSV file and creates a line plot with annotations.
    """
    # Step 1: Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: {csv_file} not found.")
        return
    
    # Step 2: Ensure proper date format
    df['date'] = pd.to_datetime(df['date'])
    
    # Step 3: Handle missing or NaN values
    df = df.dropna()  # Drop rows with missing data
    if df.empty:
        print("No data to plot after removing NaN values.")
        return
    
    # Step 4: Find the highest and lowest temperatures
    max_temp_row = df.loc[df['temperature'].idxmax()]
    min_temp_row = df.loc[df['temperature'].idxmin()]

    # Step 5: Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['temperature'], marker='o', label='Temperature')

    # Add annotations for max and min temperatures
    plt.annotate(
        f"{max_temp_row['temperature']}°C on {max_temp_row['date'].strftime('%Y-%m-%d')}",
        xy=(max_temp_row['date'], max_temp_row['temperature']),
        xytext=(max_temp_row['date'], max_temp_row['temperature'] + 2),
        arrowprops=dict(facecolor='green', arrowstyle='->'),
        fontsize=10,
        color='green'
    )
    plt.annotate(
        f"{min_temp_row['temperature']}°C on {min_temp_row['date'].strftime('%Y-%m-%d')}",
        xy=(min_temp_row['date'], min_temp_row['temperature']),
        xytext=(min_temp_row['date'], min_temp_row['temperature'] - 3),
        arrowprops=dict(facecolor='red', arrowstyle='->'),
        fontsize=10,
        color='red'
    )

    # Format the x-axis to show dates properly
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xticks(rotation=45)

    # Add labels, title, and legend
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Temperature Variations")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_temperature_data(CSV_FILE)
