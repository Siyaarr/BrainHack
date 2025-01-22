import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'EEG_recording_2025-01-22-13.40.15.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to understand its structure
print(data.head())

# Plotting each column in a separate graph
for column in data.columns[1:-1]:  # Skip the first column (index) and last column (timestamps)
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamps'], data[column], label=column)
    
    # Add labels and title
    plt.xlabel('Timestamps')
    plt.ylabel('Values')
    plt.title(f'EEG Data Visualization - {column}')
    plt.legend()
    
    # Show the plot
    plt.show()