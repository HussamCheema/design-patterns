from abc import ABC, abstractmethod


class AverageCalculator(ABC): 

    def average(self): 
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self): 
        pass

    @abstractmethod
    def next_item(self): 
        pass

    def dispose(self): 
        pass
    
    
class FileAverageCalculator(AverageCalculator):

    def __init__(self, file): 
        self.file = file
        self.last_line = self.file.readline() 

    def has_next(self):
        return self.last_line != '' 

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline() 
        return result

    def dispose(self):
        self.file.close()
        

class GeneratorAdapter:

    def __init__(self, adaptee): 
        self.adaptee = adaptee # Generator

    def readline(self):
        try:
            # Delegating next item
            return next(self.adaptee) 
        except StopIteration:
            return '' 

    def close(self): 
        pass
        
        
    
#fac = FileAverageCalculator(open('data.txt'))
#print(fac.average()) # Call the template method
        
from random import randint

# Generator doesn't keep all the numbers in memory until we consume them.
g = (randint(1, 100) for i in range(1000000)) 
fac = FileAverageCalculator(GeneratorAdapter(g)) 
print(fac.average()) # Call the template method


























