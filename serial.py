class SerialGenerator():
    """Make a new generator, starting at start"""

    def __init__(self, start=0):
        
        self.start = self.next = start
    
    def __str__(self):

        return f'The serial number is {self.start}'

    def generate(self):
        """Generate next serial number"""

        self.next = self.next + 1
        return self.next
   
    def reset(self):
        """Reset number to original start"""

        return self.start

