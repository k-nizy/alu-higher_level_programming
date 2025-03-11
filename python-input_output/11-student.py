#!/usr/bin/python3

"""
This module defines a Student class with public instance attributes and methods
to serialize and deserialize the instance.
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
            attrs (list): A list  attribute names to include in the dictionary.
                          If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key}

    def reload_from_json(self, json):
        """
        Replaces all att of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)


# Example usage:
# student = Student("John", "Doe", 23)
# j_student = student.to_json()
# print(j_student)
# student.reload_from_json({"first_name": "Jane", "age": 25})
# print(student.first_name, student.last_name, student.age)
