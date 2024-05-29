import csv
import json

def convert_csv_to_json(csv_file):
 """ Converts as CSV file to JSON format and writes it to data.sjon.

    Args:
    csv_file (str): The path to the CSV file. 

    Returns: 
        bool: True if the conversion was successful, False otherwise.
 """

#Reads CSV and Converts to Dictionaries with Error handling
  try:
    with open(csv_file, 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      data = list(reader)
  except FileNotFoundError:
    print(f"Error: File not found - {csv_file}")
    return False

# Serializing and Writing JSON Data
    with open('data.json', 'w') as jsonfile:
       json.dump(data, jsonfile)
    return True
 