print(f"\nPython Object Oriented Proegramming - MIMO App")
print(f"****************************************************\n")
#Different styles of coding are known as paradigms 
print(f"-Functional Programming")
#In functional programming, we use a lot of functions and variables. We keep data and functionality separate. We pass data into functions whenver we want something. 
def getTotal(a,b):
    return a + b
num1 = 2
num2 = 3
total = getTotal(num1, num2)
print(f"Total: {total}\n")

def getDistance(mph, h):
    return mph * h
mph = 60
h = 2
distance = getDistance(mph, h)
print(f"Distance: {distance}\n")

print("-OOP")
#In OOP we group data and functionality as properties and methods inside objects. It is useful for modeling objects, real-life or not. 
#Objects have properties and methods that we treat as one thing, like a car for example.
class Virtual_Pet:
    def __init__(self, color, name):
        self.color = color
        self.name = name
rocky = Virtual_Pet("brown", "rocky")
print(rocky.color)
print(f"{rocky.name}\n")

class Car:
    milage = 12000
    def drive(self, miles):
        self.milage += miles
tesla = Car()
tesla.drive(200)
print(f"Milage: {tesla.milage}\n")

#In OOP we use methods to update existing values of an object
class Dog:
    hungry = True
    def eat(self):
        self.hungry = False

class Piggy:
  value = 0
  def addMoney(self, amount):
    self.value = self.value + amount
    
myPiggy = Piggy()
myPiggy.addMoney(100)
print(f"Piggy bank: {myPiggy.value}\n")

print("-Encapsulating Objects")
#Encapsulation is when we group together related data and functions in the same object. 
class Cat:
  color = 'orange'
  def meow(self):
    print('Meow')

class Car:
  color = "gray"
  def drive(self):
    print("accelerating...")

#This next exaxmple is a code not encapsulated within the class
class Laptop:
  on = False

def turnOn():
  on = True

#Encapsulated code example
class Rectangle:
    base = 3
    height = 4
    def getArea(self):
        return self.base * self.height
rect = Rectangle()
area = rect.getArea()
print(f"Area: {area}\n")

print(f"****************************************************\n")

print("-Applying Inheritance in OOP")
#When we create objects one by one we run into the problem of having duplicate code. We use inheritance to make our code efficient. 
#Through inheritance, classes receive methods from other classes. We can create classes that have different properties and behaviors without coding each one from scratch.
class Parent:
  def __init__(self):
    self.eyes = "green"

class Child(Parent): #Child inherits the Parent class
  def __init__(self):
    super().__init__()
    self.age = 7

child = Child()
print("Child's eyes followed by age:")
print(child.eyes)
print(child.age)

#When defining the class we add parentheses with the class that we are inheriting
class Greetings:
    def greet(self):
        print("Hi")
class Person(Greetings):
    name = "George"
p = Person()
print("\nUsing inheritance to greet:")
p.greet()

#We can update how classes work by setting methods directly in the class
class Car: 
  def start_car(self): 
    print("Starting car") 
 
class Hybrid(Car): 
  def charge(self): 
    print("Using fuel to charge battery") 
 
class Electric(Car): 
  def fuel(self): 
    print("No fuel necessary") 
 
prius = Hybrid() 
electric = Electric() 

print("\nTwo differente classes that inherits the same class:") 
prius.start_car() 
electric.start_car() 
 
prius.charge() 
electric.fuel()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
     print("Hi!")

class Nurse(Person):
  def __init__(self, name, age):
    super().__init__("Nurse " + name, age)
  def intro(self):
    print("Hi, I'm", self.name)

person1 = Nurse("Sam", 23)
person2 = Person("Tom", 30)
print("\nNurse intro followed by person's greetings: ")
person1.intro()
person2.greet()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hi!")

class Student(Person):
  def __init__(self, name, age, major):
    super().__init__(name, age) #We code this to make sure student will have the same properties as person 
    self.major = major
student = Student("Sam", 23, "chemistry")
print("\nStudent major followed by greetings: ")
print(student.major)
student.greet()
print(f"****************************************************\n")

print("-Abstracting Objects")
#Hiding low-level functional details is called abstraction.
#Abstraction allows other developers to use a class without having to know what low-level methods it has or how they even work.
class Car:
  def __init__(self):
    self.on = False

  def injectFuel(self): #low level functionality
    print('Spraying fuel')

  def igniteFuel(self): #low level functionality
    print('Boom!')

  def startUp(self):
    self.on = True
    while self.on: #This is the abstraction part in which if on then this will happen in a loop
      self.injectFuel()
      self.igniteFuel()
car = Car()
#car.startUp() -> this will inject and ignite fuel forever infinite loop until the car is turned off

class Coffeemaker:
  def heatWater(self):
    print('Heating water')

  def brew(self): #low level functionality
    print('Adding water to grounds')

  def filterCoffee(self): #low level functionality
    print('Filtering coffee')

  def makeCoffee(self): #core method 
    self.heatWater()
    self.brew()
    self.filterCoffee()
coffeMaker = Coffeemaker()
coffeMaker.makeCoffee()

print(f"****************************************************\n")

print("-Polymorphic Objects")
#We use polymorphism to implement class behaviors differently from each other
#Polymorphism ensures that the proper method will be executed based on the calling object's class
class Feline:
  def speak(self):
    print("Meow")

class Cat(Feline):
  def lick(self):
    print("Licking paw")

class Lion(Feline):
    def prey(self):
        print("Pources on prey")
    def speak(self): #We are redefining the speak method from feline when a lion is called. Speak method is overrided 
        print("ROAR")

print("Method speak for the Cat class:")
cat = Cat()
cat.speak()
print("Method speak for the Lion class:")
lion = Lion()
lion.speak()
print(f"****************************************************\n")