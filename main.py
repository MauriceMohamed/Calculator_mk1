#console calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#function to calculate
def calculate(x,y,z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y
    else:
        return "Error"

#loop to keep the program running
answer = ""
while True:
#printing the logo
    print(logo)
    #greeting
    print("Hello, welcome to the Pythonista Calculator!")
    #asking for input
    answer = calculate(int(input("Enter the first number: ")), int(input("Enter the second number: ")), input("Enter the operator (+, -, *, /): "))
    #printing the result
    print(answer)
    #asking if the user wants to continue
    answer = input("Do you want to continue? (y/n): ")
    #if the user wants to continue, the loop will continue
    if answer == "y":
        continue
    #if the user doesn't want to continue, the loop will break
    else:
        break
#thank you message
print("Thank you for using the Pythonista Calculator!")