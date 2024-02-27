import os
import pandas as pd

def csv_to_json(input_folder, output_folder):
    print("Input Folder:", input_folder)
    print("Output Folder:", output_folder)
    # Iterate over files in input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            # Construct input and output file paths
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.replace('.csv', '.json'))
            print("Converting:", input_file, "to", output_file)
            # Read CSV file into DataFrame with alternative encoding
            try:
                df = pd.read_csv(input_file, encoding='latin1')
            except UnicodeDecodeError:
                print("Error: Could not decode file with latin1 encoding. Trying ISO-8859-1 encoding...")
                df = pd.read_csv(input_file, encoding='ISO-8859-1')
            # Write DataFrame to JSON file
            df.to_json(output_file, orient='records')
            print("Conversion complete.")

# Example usage:
csv_to_json('/Users/pkalyanakumar/Downloads/archive1', '/Users/pkalyanakumar/Downloads/archive2')