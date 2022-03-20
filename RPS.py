import random
#decide who wins, choose a random shape, work like the demo
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices = [rock, paper, scissors]

print(choices[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:\n")
print(choices[computer_choice])

if user_choice == 0:
    if computer_choice == 0:
        print("Tie game!")
    elif computer_choice == 1:
        print("You lose.")
    else:
        print("You win!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("Tie game!")
    else:
        print("You lose.")
else:
    if computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("Tie game!")

#Solution
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")


