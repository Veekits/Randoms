import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import re

base_dir = 'C:/Users/VMUKITA/OneDrive - Goodlife Pharmacy/Desktop/MY PROJECTS/Randoms/Web Scraping/OUTPUT/Excel Attachments'

def clean_quantity(quantity):
    # Remove non-numeric characters and specific strings
    cleaned_quantity = re.sub(r'[^0-9.]', '', str(quantity))
    return int(float(cleaned_quantity)) if cleaned_quantity else None

def extract_codes_and_quantities(directory):
    # Create a list to store the file paths
    file_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    # Sort the file paths based on their index in the folder name
    file_paths.sort(key=lambda x: int(os.path.basename(os.path.dirname(x)).split('_')[0]))

    # Initialize a label encoder for categorical encoding
    label_encoder = LabelEncoder()

    for file_path in file_paths:
        try:
            # Read the Excel file
            df = pd.read_excel(file_path)

            # Identify columns with codes and quantities
            code_columns = [col for col in df.columns if 'code' in str(col).lower() or 'item no.' in str(col).lower()]
            quantity_columns = [col for col in df.columns if 'quantity' in str(col).lower() or 'qty' in str(col).lower()]

            if code_columns and quantity_columns:
                # Extract data from identified columns
                codes_raw = df[code_columns].values.flatten()
                quantities_raw = df[quantity_columns].values.flatten()

                # Clean codes and quantities
                codes = [int(code) if pd.notna(code) else None for code in codes_raw]
                quantities = [clean_quantity(q) for q in quantities_raw]

                # Filter out entries where the cleaned quantity is not None
                non_empty_entries = [(code, quantity) for code, quantity in zip(codes, quantities) if code is not None and quantity is not None]

                # Print the results
                folder_name = os.path.basename(os.path.dirname(file_path))
                print(f"Folder: {folder_name}, File: {os.path.basename(file_path)}")
                for code, quantity in non_empty_entries:
                    print(f"Code: {code}, Quantity: {quantity}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# Call the function with the base directory
extract_codes_and_quantities(base_dir)