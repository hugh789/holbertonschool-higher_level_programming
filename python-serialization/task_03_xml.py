import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
  """Serializes a Python dictionary to XML and saves it to a file.

  Args:
      dictionary (dict): The Python dictionary to serialize.
      filename (str): The filename to save the XML data.
  """
  root = ET.Element("data")  # Create the root element

  for key, value in dictionary.items():
    # Add child elements with tag as key and text as value (converted to string)
    element = ET.SubElement(root, key)
    element.text = str(value)

  # Write the XML tree to the file
  with open(filename, "wb") as f:
    ET.indent(root, space="  ", level=0)  # Optional: Add indentation
    ET.write(f, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
  """Deserializes XML data from a file and returns a Python dictionary.

  Args:
      filename (str): The filename of the XML file.

  Returns:
      dict: The deserialized Python dictionary.
  """
  try:
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Create an empty dictionary to store deserialized data
    deserialized_dict = {}
    for child in root:
      # Extract tag (key) and text (value) from child elements
      deserialized_dict[child.tag] = child.text

    return deserialized_dict
  except FileNotFoundError:
    print(f"Error: File not found - {filename}")
    return None


# Example usage (can be placed outside the functions for reusability)
if __name__ == "__main__":
  sample_dict = {"name": "John", "age": 28, "city": "New York"}
  xml_file = "data.xml"

  serialize_to_xml(sample_dict, xml_file)
  print(f"Dictionary serialized to {xml_file}")

  deserialized_data = deserialize_from_xml(xml_file)
  print("\nDeserialized Data:")
  print(deserialized_data)
