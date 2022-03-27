def greet():
    print("Hello darkness my old friend")
    print("How are you?")
    print("JOSH JOSH JOSH?")

greet()

def greet_with_name(name):
    print(f"Hello how are you {name}?")
    print(f"How has your day been {name}?")

greet_with_name("Asvinth")

def greet_with(name, location):
    print(f"Hello there {name}, how is life in {location}")

greet_with(location = "Endeavour Hills", name = "Asvinth")



#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need {num_of_cans}.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)





#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
