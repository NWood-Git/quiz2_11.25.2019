import random

class Number():
    random_lower = 0
    random_upper = 100

    def __init__(self, value):
        self.value = value

    def __str__(self):
        class_name = type(self).__name__
        return f"<{class_name} {self.value}>"
        
    @classmethod
    def random(cls):
        value = random.randrange(Number.random_lower,Number.random_upper)
        return value
    
    

five = Number(5)
print(five)

Number.random_lower = 1000
Number.random_upper = 10000
rand = Number(Number.random()) #changed line from rand = Number.random() from the question to this
print(rand)