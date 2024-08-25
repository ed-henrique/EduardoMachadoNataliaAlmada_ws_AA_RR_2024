import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('results.csv', delimiter=';')

# Extract input type and input size from the 'Input' column
df['Input_Type'] = df['Input'].apply(lambda x: x[0])  # 'o', 'a', or 'd'
df['Input_Size'] = df['Input'].apply(lambda x: int(x.split('-')[1]))

# Filter data for ascending, descending, and random orders
ascending_data = df[df['Input_Type'] == 'o']
descending_data = df[df['Input_Type'] == 'd']
random_data = df[df['Input_Type'] == 'a']

# Define a function to plot the data
def plot_data(ax, data, input_type):
    # Sort the data by 'Input_Size' to ensure plots are ordered
    data = data.sort_values('Input_Size')
    
    # Plot the actual time taken by each algorithm
    for algo in data['Algorithm'].unique():
        algo_data = data[data['Algorithm'] == algo]
        ax.plot(algo_data['Input_Size'], algo_data['Time'], label=f'{algo.capitalize()} Sort')
    
    # Add expected time complexity lines based on merge sort
    input_sizes = np.array(data['Input_Size'])
    quick_sort_data = data[data['Algorithm'] == 'quicksort']
    merge_sort_data = data[data['Algorithm'] == 'mergesort']

    if len(input_sizes) > 0:
        n_log_n = input_sizes * np.log2(input_sizes)
        n_squared = input_sizes ** 2

        # Use a scaling factor that aligns with the average runtime of the merge sort
        scale_factor_nlogn = np.mean(merge_sort_data['Time']) / np.mean(n_log_n)
        scale_factor_nsq = np.mean(quick_sort_data['Time']) / np.mean(n_squared)

        # Scale the complexity curves
        n_log_n_scaled = n_log_n * scale_factor_nlogn
        n_squared_scaled = n_squared * scale_factor_nsq

        # Plot the scaled curves
        ax.plot(input_sizes, n_log_n_scaled, 'k--', label='O(n log n)')
        ax.plot(input_sizes, n_squared_scaled, 'r--', label='O(n²)')
    
    ax.set_xlabel('Input Size')
    ax.set_ylabel('Time')
    ax.set_title(f'Algorithm Performance for {input_type} Input')
    ax.legend()
    ax.grid(True)

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Plot each type of input data on a different subplot
plot_data(axs[0], ascending_data, 'Ascending')
plot_data(axs[1], descending_data, 'Descending')
plot_data(axs[2], random_data, 'Random')

# Adjust layout for better spacing between subplots
plt.subplots_adjust(hspace=0.6)  # Increase hspace for more vertical space between subplots

# Show the plots
plt.show()
