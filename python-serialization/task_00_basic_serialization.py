import json


def serialize_and_save_to_file(data, filename):
  """
  Serializes a Python dictionary to a JSON file.

  Args:
      data: A Python dictionary to serialize.
      filename: The filename of the output JSON file.
  """
  with open(filename, 'w') as f:
    json.dump(data, f, indent=4)  # indent for readability


def load_and_deserialize(filename):
  """
  Loads and deserializes a JSON file to a Python dictionary.

  Args:
      filename: The filename of the input JSON file.

  Returns:
      A Python dictionary with the deserialized JSON data from the file.
  """
  with open(filename, 'r') as f:
    return json.load(f)


# My data
my_data = {"name": "John Doe", "age": 30, "city": "New York"}

# Serialize and save to file (replace 'data.json' with your desired filename)
serialize_and_save_to_file(my_data, 'data.json')

# Load and deserialize
deserialized_data = load_and_deserialize('data.json')

print(deserialized_data)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York'}