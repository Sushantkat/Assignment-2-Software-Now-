import os
import pandas as pd
import shutil

csv_folder_path = r'C:\Users\susha\OneDrive\Desktop\SOFTWARE NOW\Assignment 2\data'
output_txt_file = 'allcsvs.txt'

# Getting a list of CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder_path) if file.endswith('.csv')]

# Extracting text from multiple columns in CSV files
texts = []

for csv_file in csv_files:
    csv_path = os.path.join(csv_folder_path, csv_file)
    df = pd.read_csv(csv_path)
    
    # Concatenating text from all columns
    text_concatenated = ' '.join(str(cell) for row in df.itertuples(index=False) for cell in row)
    
    texts.append(text_concatenated.strip())

# Saving the concatenated text to a single .txt file
with open(output_txt_file, 'w', encoding='utf-8') as file:
    for text in texts:
        file.write(str(text) + '\n')