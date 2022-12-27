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

print(f"****************************************************\n")

print("-Conditionals and functions")
def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")
add_shipping(54)
add_shipping(189)

def calculate(operator, x, y):
  if operator == "+":
    print(x + y)
  else:
    print(f"unknown: {operator}")
calculate("-", 30, 10)

print(f"****************************************************\n")

print("-Functions with lists")
def display_programme(movies):
    print(f"Airing tonight: {movies}")
    print(f"Total movies: {len(movies)}")
movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def get_winner(top_players):
  winner = top_players[0]
  print(f"Game winner: {winner}")
top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)

def update_first_place(leaderboard, player):
    leaderboard[0] = player
    return leaderboard
leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)

def set_initials(names, initial):
  names[0] = initial
  return(names)
author_names = ["Francis", "Scott", "Fitzgerald"]
author_names = set_initials(author_names, "F.")
print(author_names)

print(f"****************************************************\n")

print("-Functions with loops")
#Functions help us reuse loops by allowing us to chane the number of repetitions or the list we are iterating through
def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1
onboard_passengers(4)

def display_progress(total_files):
    for i in range (total_files):
        print(f"Downloading file {i+1} out of {total_files}")
display_progress(3)

#loop that iterates through a list
def halve_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")
cart_list=[5, 20, 80]
halve_prices(cart_list)

def show_next_track():
    playlist = ["Hey Jude", "Helter Skelter", "Something"]
    for track in playlist:
        print(f"Next up: {track}")
show_next_track()

print(f"****************************************************\n")

print("-Morse Code")
def convert_to_morse(code):
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("6", "-----")
    return code
lock_code = "1 2 2 5 0"
print(f"Initial code: {lock_code}")
morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")

print(f"****************************************************\n")

print("-Calculator")
def calculator(num1, num2, op):
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print(f"Unknown: {op}")
    operation = f"{num1} {op} {num2} = {result}"
    return operation
print(calculator(2,3,"+"))        
