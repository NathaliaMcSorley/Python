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
print(f"****************************************************\n")

