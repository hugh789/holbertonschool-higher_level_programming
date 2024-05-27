#!/usr/bin/python3
"""this module is about creating an abstract class named Shape using the ABC
package."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
  """
  Abstract class representing a shape.
  """

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Circle(Shape):
  """
  Concrete class representing a circle.
  """

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return pi * self.radius**2

  def perimeter(self):
    return 2 * pi * self.radius

class Rectangle(Shape):
  """
  Concrete class representing a rectangle.
  """

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

def shape_info(shape):
  """
  Prints the area and perimeter of a shape object.
  """
  print(f"Area: {shape.area()}")
  print(f"Perimeter: {shape.perimeter()}")

# Test cases
circle = Circle(5)
rectangle = Rectangle(4, 6)

shape_info(circle)
print("---")
shape_info(rectangle)