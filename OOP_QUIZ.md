## Phase 1 Week 2 Quiz

Properties and methods are instance properties and methods unless otherwise
specified

### 1: init & string representation

Write a class called Car with three properties: make, model, year.

The constructor should take three optional arguments, make, model, and year
that set the properties accordingly. If an argument is absent, it should
set that property to ""

The string representation should show the name of the class and the values
of the three properties.

```
outback = Car("Subaru", "Outback", "1999")
print(outback.year)
# prints 1999
print(outback)
# prints something like:
# <Car 1999 Subaru Outback>
```

### 2: inheritance

#### pt 1: modules & imports

For this problem create a new directory to contain your answer. Create a file
called test.py in that folder. Create a subdirectory called app. The classes
in this question should be written in one or more python files inside of
app.

inside test.py you should be able to do something like

```
# from app.vehicle import Vehicle

v = Vehicle()

# or
# import app.model

c = app.model.Car()

# or similar. 
```

The requirement is that the classes be imported from a file in the base of the
project from a subdirectory called app

#### pt 2: parent & child classes

test.py should import your classes and have code that demonstrates the features
of the classes that the questions ask for.

Create a class called Vehicle that has two properties, weight and max_speed.
These properties are integers and can be set by optional arguments to the 
constructor. The default values should be None.

```
bumper_car = Vehicle("400 lbs", "5 mph")
print(bumper_car.weight)
# prints "400 lbs"
```

Create a class called Airplane that is a child class of Vehicle. It has
a property called max_altitude and a make property. It also has weight and
top speed. It sets all four properties with optional arguments to the constructor.
The `__init__` method for Airplane should call its parent's `__init__` method
to set weight and top speed. The default values should be None.

```
cessna = Airplane(max_altitude="15,000 ft", max_speed="130 mph")
print(isinstance(cessna, Airplane))
# prints True
print(isinstance(cessna, Vehicle))
# prints True
print(cessna.max_speed)
# prints "130 mph"
```

Create a class called TrainCar that is a child class of Vehicle. It has
a property called line that is set with an optional argument to the constructor.
The TrainCar's weight should default to "65 tons" and its top speed should
default to "150 mph" if they are not set by arguments.

```
amtrak = Traincar()
print(amtrak.weight)
# prints "65 tons"
```

### 3: class methods

Create a class called Number. It has one instance property, value that can be
set by the constructor.

Its string representation should show the value in some way.

Number has two class properties, random_lower and random_upper. They default
to 0 and 100.

Number has one class method, random. It takes no additional arguments. It
returns a new Number object with a random value where 

(use random.randrange)

Number.random_lower <= value < Number.random_upper

```
five = Number(5)
print(five)
# prints "<Number 5>" or something similar
Number.random_lower = 1000
Number.random_upper = 10000
rand = Number.random()
print(rand)
# prints "<Number 4528>" or something similar with a random value between
# 1000 and 9999
```

### 4: bonus: dunder methods

Make it so your Number class evaluates to False in an if statement if 
value is 0.

```
nothing = Number(0)
if nothing:
    print("oops")
else:
    print("works")

# prints("works")
```
