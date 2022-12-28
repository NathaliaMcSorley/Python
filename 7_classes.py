print(f"\nPython Classes - MIMO App")
print(f"****************************************************\n")
#Classes help us group data and functionality. A class is a template that we use to create many similar but distinct things. 
#By using a template, we can create different configurations without having to create individual variables.

class Computer: #class template start here
  def __init__(self, size, storage):
   self.size = size
   self.storage = storage

  def print_specs(self):
    print("Display size: " + self.size)
    print("Storage size: " + self.storage)

low_spec = Computer("13", "256GB") #that is how we create an instance
mid_spec = Computer("15", "512GB") #Computer is the definition/class and mid_spec is an instance
high_spec = Computer("17", "1TB")
premium_spec = Computer("17", "2TB")

print("Accessing a variable:")
print(low_spec.size) #Accessing a class variable instance.variable
print(low_spec.storage) #Accessing a class variable

print(f"\nAccessing the method of the class:")
low_spec.print_specs()

#Classes can have functions too, which are known as methods when they are inside of a class
#self is a special keyword that we need to use inside our class definition. We pass self as the first parameter to all the methods we add.
class Virtual_Pet:
  color = "brown"
  legs = 4

  def bark(self):
    print("Bark")

  def display_color(self):
    print(self.color)

  def display_legs(self):
    print(self.legs)

rocky = Virtual_Pet()
print(f"\nAccessing the methods of the class:")
rocky.bark()
rocky.display_color()
rocky.display_legs()
print(f"****************************************************\n")

print("-Constructor method")
#We can use constructor method to make creating different instances from a class more flexible
class Virtual_Pet:
    def __init__(self, color, legs): #allow us to set unique values for the class variable's when we create an instance
        self.color = color #This sets the value
        self.legs = legs
    
    def display_color(self):
        print(self.color)
    
    def display_legs(self):
        print(self.legs)

rocky = Virtual_Pet("brown", 3)
benny = Virtual_Pet("black", 4)

print("Accessing a variable:")
print(rocky.color)
print(rocky.legs)

print(f"\nAccessing the methods of the class:")
benny.display_color()
benny.display_legs()

class Pie:
  def __init__(self, flavor, ingredients):
    self.flavor = flavor
    self.ingredients = ingredients

  def print_ingredients(self):
    for i in self.ingredients:    
      print(i)

applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter'])
print(f"\nAccessing the methods of the class:")
applePie.print_ingredients()

class Book_Series:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.num_books = len(books)

    def print_name(self):
        print(self.name)

    def print_books(self):
        print(self.books)

hg = Book_Series("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])
print(f"\nAccessing the methods of the class:")
hg.print_books()
print("Accessing a variable:")
print(hg.num_books)
print(f"****************************************************\n")