class SquareNumbers:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current ** 2
        self.current += 1
        return value 
for num in SquareNumbers(5):
    print(num)