import pickle


class CustomObject:
  """
  A custom class to represent a person with attributes like name, age, and student status.
  """
  def __init__(self, name, age, is_student):
    self.name = name
    self.age = age
    self.is_student = is_student

  def display(self):
    """
    Prints the object's attributes in a user-friendly format.
    """
    student_status = "True" if self.is_student else "False"
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Is Student: {student_status}")

  def serialize(self, filename):
    """
    Serializes the object and saves it to a file using pickle module.

    Args:
      filename (str): The name of the file to save the serialized object.

    Returns:
        None
    """
    try:
      with open(filename, "wb") as f:
        pickle.dump(self, f)
    except (IOError, pickle.PicklingError) as e:
      print(f"Error serializing object: {e}")

  @classmethod
  def deserialize(cls, filename):
    """
    Deserializes an object from a file using pickle module.

    Args:
      filename (str): The name of the file containing the serialized object.

    Returns:
        CustomObject: The deserialized object, or None if an error occurs.
    """
    try:
      with open(filename, "rb") as f:
        return pickle.load(f)
    except (IOError, pickle.UnpicklingError) as e:
      print(f"Error deserializing object: {e}")
      return None