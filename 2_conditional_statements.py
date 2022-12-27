print(f"\nPython Conditional Statements - MIMO App")
print(f"****************************************************\n")

print("-If statement")
#Use to write code that adapts to different situation. The if statement runs code only i fthe boolen it's relying on is True
if True:
    print("Hello")

greetings = True
if greetings:
    print("Hello Again")

greetings = "Hello"
if greetings == "Hello":
    print("Hello Once Again")

#if you want to skip the code set the boolean to false 
if False:
    print("skip the code")

greetings = False
if greetings:
    print("skip the code")

if greetings == True:
    print("first option")
else:
    print("second option")

score = 10
if score == 10:
    print("Score is 10")
elif score < 10:
    print("score less than 10")
else:
    print("Score more than 10")

email = "johnson@email.com"
is_duplicate = True
if is_duplicate:
    print(f"{email} is already in use")
print(f"****************************************************\n")

print("-While loop")
#Infinite loop 
#while True: 
#    print ("Infinity loop")

counter = 1
while (counter < 10):
    print(counter)
    counter+=1

print(f"****************************************************\n")

print("-For loop")
for i in range (5):
    print(f"Hello {i}")

print(f"****************************************************\n")
#Check if a number is an outliner in the dataset and set the variable outlier to be True if it is
upper_limit = 91
lower_limit = 24
outlier = False
number = 9 

if number > upper_limit:
    outlier = True
if number < lower_limit:
    outlier = True
if outlier == True:
    print(f"{number} is an outlier \n")

#if, elif and else example
ride_type = "Black"
credits = 4
ride_price = 0 
final_price = 0

if ride_type == "DooberX":
    ride_price = 20.5
elif ride_type == "Balck":
    ride_price = 38.9
else:
    ride_price: 19.2

print(f"Ride Price: {ride_price}")

if credits > 0:
    final_price = ride_price - credits
print(f"Final price: {final_price} \n")

#piece together different parts of a link to give users a 50% discount when signing up with the link
base = "www.homeflix.com"
coupon = "signup/coupon"
discount = 50
amount = 4

for num in range (amount):
    print(f"{base}/{coupon}/{discount}/{num}")
print(f"{amount} coupons created\n")

#Compound Interest Calculator
account = 100
interest_rate = 0.004
years = 3

print(f"Initial Amount: {account}")

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"year {counter}: {account}")
    counter+=1
print(f"****************************************************\n")