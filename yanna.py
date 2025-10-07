def greet_user(user_name):
    print(f"Hello, {user_name}! ")
def get_fun_fact(num):
    if num == 1:
        return "Ganda mo today!"
    elif num == 2:
        return "Sobrang blooming mo!"
    elif num == 3:
        return "I like your outfit!"
    elif num == 4:
        return "Don't forget to smile :)"
    else:
        return "Sorry, I don't have a fun fact for that number. Pick 1-5."
def goodbye(user_name): 

    print(f"\nGoodbye {user_name}! Thanks for trying the friendly Greeter Bot. :) ") 
user_name = input("What is your name?")
try: 

     num = int(input("To get a fun fact, Pick a number 1to 5."))

except ValueError: 

     print("That wasn't a number. Please enter an integer like 1, 2, 3, 4, or 5.") 

fun_fact = get_fun_fact (num)

print(fun_fact)
goodbye(user_name)
