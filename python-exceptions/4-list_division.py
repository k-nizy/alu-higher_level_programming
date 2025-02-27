#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Try to perform the division
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            quotient = 0
        except (TypeError, ValueError):
            # Handle wrong types
            print("wrong type")
            quotient = 0
        except IndexError:
            # Handle out-of-range access
            print("out of range")
            quotient = 0
        finally:
            # Append the result to the list
            result.append(quotient)
    return result
