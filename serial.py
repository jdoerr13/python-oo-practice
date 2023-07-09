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
    def __init__(self, start = 0): # start is option value, if no value provided, will start at 0
        self.start = self.next = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"
        
    def generate(self):
        self.next += 1
        return self.next -1 #first return the previously generated serial number
    
    def generate(self):
        self.next += 1
        return self.next -1
