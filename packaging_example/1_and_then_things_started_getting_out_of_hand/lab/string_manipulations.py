# String Manipulations
def uppercase(string):
    """Return string converted to uppercase."""
    return string.upper()

def backwards(string):
    """Return string, but backwards."""
    return string[::-1]
    # Could also be:
    # return ''.join(reversed(string))
