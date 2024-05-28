import json

# Load data from JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Print the loaded data
print("Loaded data:", data)

# Access specific data elements (optional)
name = data["name"]
age = data["age"]

print(f"Hello, {name}! You are {age} years old.")