#We can use functions to gorup related code and perform the task in one place.
#def function_name(): -> keyword to define a function 
print(f"\nPython Functions - MIMO App")
print(f"****************************************************\n")

print("-Functions and parameters")
def greet_user():
    name = "Anna"
    print(f"Good morning, {name}")
    print("Welcome back")
greet_user()

#To pass a value to a function, we first add a variable called a parameter inside the parentheses of the function
def greet(name):
    print(f"Hello, {name}")
greet("April")

def display_half(number):
    half = number / 2
    print(half)
display_half(10)

#A function can return a value to the code that called it. If we don't include a return statement, the fucntion returns the value none instead
def age_label(age):
    label = "User age: " + age
    return label
result = age_label("29")
print(result)

def half_twice(number):
    half = number / 2
    half_again = half / 2
    return half_again
result = half_twice(12)
print(result)
print(f"****************************************************\n")

print("-Multiple parameters")
def display(first, last):
    print(first + ", " + last)
display("Alex", "Morgan")

#Functions are actions, so their names often starts with a verb
def create_email(name, year):
    return name + year + "@hutmail.com"
email = create_email("jo", "1998")
print(email)

#Functions that return values often start with verbs like get, compute, calculate
def get_telephone(prefix, number):
    return prefix + number
print(get_telephone("290 ", "87639878"))

def get_sum(num_1, num_2):
    return num_1 + num_2
print(f"Sum function: {get_sum(1, 3)}")

def calculate_sum(num_1, num_2):
  return num_1 + num_2

def calculate_difference(num_1, num_2):
  return num_1 - num_2

#As a special case, functions that return boolean values often start with is, has, can
def is_freezing(temperature):
    return temperature < 0
freezing = is_freezing(-3)
print(f"Is it freezing today? {freezing}")

#A function is like a black box because when it has a descriptive name, we can call it wihout reading the code inside it
#A function's output and input can have different types. 
def is_renting_age(age):
    print(age >= 25)
is_renting_age(22)

def is_renting_age(age):
    return age >= 25
can_rent_car = is_renting_age(26)
print(f"Can this person rent a car? {can_rent_car}")

print(f"****************************************************\n")

print("-Variable Scope")
#Variables created inside a function have a local scope and can only be accessed or updated wihtin the function that created it
def add_bonus(salary):
    bonus = 100
    print(f"Salary plus bonus: {salary + bonus}")
add_bonus(1900)

#Variables created outside of a function block have a global scope and can be safely accessed anywhere in the code
#All variables, except for those created inside functions, have a global scope (including variables created inside conditionals and loops)
shipping = 10
def calculate_total(cart):
    print(f"Total amount: {cart + shipping}")
calculate_total(54)