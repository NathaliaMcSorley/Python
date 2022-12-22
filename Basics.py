# Snake Case: Variable names with multiple words, use '_', such as home_city
# = assigns a value to a variable while == is an operator that compares two values  
print(f"\nPython Intro - MIMO App")
print(f"****************************************************\n")

print("-Update Variable")
status = "Watching Netflix" 
print(status)
status = "Styding Pyton" # = assigns a new value to the same variable
print(status)

print(f"\n-Store new value in another variable")
new_status = "Cooking a meal" # = assigns another value to a new variable
status = new_status # = assigns a variable to another variable 
print(new_status)
print(status)
print(f"****************************************************\n")

print("-True, False and the not operator")
correct = True
incorrect = not True #False
print(correct)
print(incorrect)
correct = False
incorrect = not False #True
print(correct)
print(incorrect)
available = True
out_of_stock = not available
print(not available) #False
print(out_of_stock)
print(f"****************************************************\n")

print("-Operators used for comparison")
print(10==10) #equality operator
print(10!=10) #inequality operator
print(10<=10) #less than or equal operator
print(10<10) #less operator
print(10>=10) #greater than or equal operator
print(10>10) #greater operator
print("apple"=="apple") 
print("subscribed"!="unsubscribed")
print(f"****************************************************\n")

print("-Variable Types")
sugar_content="High" #String
print(sugar_content)

score = 42 #Integer
print(score)

pi = 3.14159
print(pi) #Float

is_on = True #Boolean
print(is_on)
print(f"****************************************************\n")

print("-Formatted Strings")
#Allow us to display expressions like adding a string to a number, wihtout any error
print(f"{2} new messages")
messages_unread = 4
print(f"{messages_unread} new messages")
print(f"****************************************************\n")