import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the main folder containing subfolders with .txt files
folder_path = '/Users/josuecampos/Downloads/20240611 test98/Activation 2V_24h'


# Function to read and process a single .txt file
def read_txt_file(file_path):
    # Example: assuming each .txt file contains two columns of data separated by semicolons
    data = pd.read_csv(file_path, sep=';')
    data['Current Density (A/cm2)'] = data['WE(1).Current (A)'] / 5
    return data


# Walk through all subdirectories and list all .txt files
for root, dirs, files in os.walk(folder_path):
    txt_files = [f for f in files if f.endswith('.txt')]

    # Process each .txt file in the current directory
    for txt_file in txt_files:
        file_path = os.path.join(root, txt_file)
        data = read_txt_file(file_path)

        # Create a graph
        plt.figure()
        plt.scatter(data['Time (s)'], data['Current Density (A/cm2)'], marker='o')
        plt.title(f'Graph for {txt_file}')
        plt.xlabel('Time (s)')
        plt.ylabel('Current Density (A/cm2)')

        # Save the graph as an image file in the same directory as the .txt file
        output_image_path = os.path.join(root, f'{os.path.splitext(txt_file)[0]}.png')
        plt.savefig(output_image_path)
        plt.close()

print("Graphs have been created and saved successfully.")

