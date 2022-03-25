import random
from hangman_util import logo, word_list, stages

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")


guess_list = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    
    if guess in guess_list:
      print(f"You have already guessed {guess}")
    else: 
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      if guess not in chosen_word:
        print(f"You guessed {guess} and it was not in the word. You lose a life")

        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose.")

      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
      guess_list.append(guess)
      print(stages[lives])