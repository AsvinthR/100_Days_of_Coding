import random
#
random_integer = random.randint(1, 10)
print(random_integer)

#you multiply by 5 because it will normally give you a float between 0 and 1 but this makes it up to any number you deem (0.9999999 * x)
random_float = random.random() * 5
print(random_float)

love_score_1 = random.randint(1, 100)
print(f"Your love score is {love_score_1}")

HEADS_OR_TAILS
choice = random.randint(0, 1)
if choice == "1":
    print("Heads")
else:
    print("Tails")


#Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
print(states_of_america[3])

states_of_america[1] = "Pencilvania"
print(states_of_america)

#to add to the list
states_of_america.append("Asvinthland")
print(states_of_america)

states_of_america.extend(["Kevin", "Jack"])
print(states_of_america)

#BANKER_ROULETTE
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_names = len(names)
random_choice = random.randint(0, total_names - 1)
payee = names[random_choice]
print(payee + " is going to buy the meal today!")


#Index errors and nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])