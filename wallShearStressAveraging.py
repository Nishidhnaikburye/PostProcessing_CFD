import numpy as np
import matplotlib.pyplot as plt

import os
import csv

def process_wss_file(file_path):
    # Read the .dat file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize lists to store time and vector data
    time = []
    vectors = []

    # Parse the data
    for line in lines:
        if line.startswith("#"):
            continue
        else:
            parts = line.split("\t")
            time.append(float(parts[0]))
            vector_str = parts[1].strip()[1:-1]  # Remove parentheses
            vector = [float(x) for x in vector_str.split()]
            vectors.append(vector)

    # Convert lists to numpy arrays for easier manipulation
    time = np.array(time)
    vectors = np.array(vectors)

    # Calculate magnitude for each vector at each time step
    vector_magnitudes = np.linalg.norm(vectors, axis=1)

    return time, vector_magnitudes

# File paths
inner_file_path = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/avgWSSInner/avgWSSInner.dat"
outer_file_path = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/avgWSSInner/avgWSSOuter.dat"
csvExport_path = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/csvExport/"
# Process inner and outer files
inner_time, inner_magnitudes = process_wss_file(inner_file_path)
outer_time, outer_magnitudes = process_wss_file(outer_file_path)

# Plot inner and outer WSS across time
plt.plot(inner_time, inner_magnitudes, label='Inner WSS')
plt.plot(outer_time, outer_magnitudes, label='Outer WSS')
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.title('Inner and Outer WSS Across Time')
plt.legend()
plt.grid(True)
plt.show()



def save_to_csv(time_data, magnitude_data, filename, folder_path):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Magnitude'])
        for time, magnitude in zip(time_data, magnitude_data):
            writer.writerow([time, magnitude])

# Usage example:
csvExport_path = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/csvExport/"
save_to_csv(inner_time, inner_magnitudes, 'inner_wss.csv', csvExport_path)
save_to_csv(outer_time, outer_magnitudes, 'outer_wss.csv', csvExport_path)




# Calculate average magnitude for inner and outer WSS
inner_avg = np.mean(inner_magnitudes)
outer_avg = np.mean(outer_magnitudes)

# Print average magnitudes
print("Average Inner WSS Magnitude:", inner_avg)
print("Average Outer WSS Magnitude:", outer_avg)


print("WSS ratio: ", inner_avg/outer_avg)