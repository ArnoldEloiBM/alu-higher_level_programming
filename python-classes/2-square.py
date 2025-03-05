class Square:
    """A class that defines a square with a private size attribute."""
    
    def __init__(self, size=0):
        """Initializes the square with a private size attribute.
        Ensures size is a non-negative integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

