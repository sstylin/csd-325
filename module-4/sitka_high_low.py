

# Program modify by Steve Stylin
# Bellevue University, Module 4.2 Assignment: High/Low Temperatures
print("\nProgram modify by Steve Stylin\n Bellevue University,\nModule 4.2 Assignment: High/Low Temperatures ")
import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

def main():
    filename = 'sitka_weather_2018_simple.csv'
    
    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        choice = input("Please select an option (1, 2, or 3): ")

        if choice == '1':
            plot_temperatures(filename, 'high')
        elif choice == '2':
            plot_temperatures(filename, 'low')
        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def plot_temperatures(filename, temp_type):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])  # Assuming low temperatures are in the 6th column
            highs.append(high)
            lows.append(low)

    # Plot the selected temperatures.
    fig, ax = plt.subplots()
    if temp_type == 'high':
        ax.plot(dates, highs, c='red', label='High Temperatures')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
    else:
        ax.plot(dates, lows, c='blue', label='Low Temperatures')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)

    # Format plot.
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()