"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Create serial number starting at provided value"
        self.start = self.next = start

    def __repr__(self):
        "representation of class"
        return f"<SerialGenerator. Start = {self.start}, Next = {self.next}.>"

    def generate(self): 
        "generate new serial number one value greater than the previous"
        self.next += 1
        return self.next -1 
    
    def reset(self):
        "reset number to original start value"
        self.next = self.start
