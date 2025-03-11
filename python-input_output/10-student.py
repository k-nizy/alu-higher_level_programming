#!/usr/bin/python3

"""
This module defines a Student class with public instance attributes and a method
to retrieve a dictionary representation of the instance, optionally filtering
attributes based on a list of attribute names.
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to include in the dictionary.
                          If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes.
        """
        if attrs is None:
            # Explicitly specify the order of keys
            return {
                'age': self.age,
                'last_name': self.last_name,
                'first_name': self.first_name
            }
        else:
            # Filter attributes based on the provided list and maintain order
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}


# Example usage:
# student = Student("John", "Doe", 23)
# j_student = student.to_json()
# print(j_student)
