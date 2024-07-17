#!/usr/bin/python3
"""Define a square class"""


class square():
    """Square Class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the square class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create an instance of the square class"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
