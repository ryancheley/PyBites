class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.length * self.length

    def __str__(self):
        """Returns a string representation of the table"""
        result = ''
        for i in range(self.length):
            for j in range(self.length):
                multiplication = (i+1) * (j+1)
                if j < self.length-1:
                    result += f' {multiplication} |'
                else:
                    result += f' {multiplication}'
            result += '\n'
        return result

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x > self.length or y > self.length:
            raise IndexError
        return x * y


test = MultiplicationTable(3)
print(test)