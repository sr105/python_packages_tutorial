# Computations
def multiply_a_list_by(a_list, number):
    """Return a list with every item multiplied by number."""
    return [item * number for item in a_list]


def square_a_list(a_list):
    """Return a list with every item squared."""
    return [item * item for item in a_list]


# Constants
PI = 3.14159
AVOGADRO = 6.0221409e23
EULER = 2.718281


# String Manipulations
def uppercase(string):
    """Return string converted to uppercase."""
    return string.upper()

def backwards(string):
    """Return string, but backwards."""
    return string[::-1]
    # Could also be:
    # return ''.join(reversed(string))
