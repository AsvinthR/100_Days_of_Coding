print('''
⣿⣿⡿⠟⠛⠛⣿⠛⠛⠛⠛⢻⠛⠛⠛⢻⡟⠛⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠐⠿⣿⣿⣿⡇⢸⣿⣿⠄⢸⣿⣿⡇⠄⣿⣿⠄⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣶⣤⠈⣿⣿⡇⢸⣿⣿⠄⢰⣶⣾⡇⠄⣿⣿⠄⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣇⣉⣁⣤⣿⣿⣇⣸⣿⣿⣀⣸⣿⣿⣿⣤⣈⣁⣤⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⢿⣿⡿⠿⣿⡿⢿⡿⠿⠿⠿⣿⡿⠿⠿⠿⣿⠿⠿⠿⠿⣿⣿⠿⠟⠿⣿
⡇⠈⣿⠄⠄⣿⠃⣸⡇⠄⣶⣶⣿⡇⢰⣶⣶⣿⠄⢸⡷⠄⣿⡇⠰⢿⣶⣿
⣿⠄⠋⢰⡆⠸⠄⣿⡇⠄⣤⣤⣿⡇⢠⣤⣤⣿⠄⢰⣤⠈⢻⣿⣦⣄⠈⢿
⣿⣇⣀⣾⣷⣀⣸⣿⣇⣀⣉⣉⣹⣇⣈⣉⣉⣿⣀⣈⣉⣠⣾⣋⣉⣉⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
print("Welcome to a classic Crafty BoisTM night out.")
print("Your objective is to have a classic awesome night out.\n")

choice1 = input("You arrive at Savo's house and he asks you which anime you want to watch together? Jujutsu Kaisen or Demon Slayer? \n").lower()
if choice1 == "jujutsu kaisen":
    choice2 = input("You have a great time and end up meeting Kuvindu for dinner where he starts talking about kpop. Do you listen? Yes or No? \n").lower()
    if choice2 == "no":
        choice3 = input("Thank god you did not put up with that. You finally decide to get some desert but where does Pranav want to get desert? Deserts by Night, Vanilla or Maccas? \n").lower()
        if choice3 == "deserts by night":
            print("You had a classic awesome night out!")
        elif choice3 == "vanilla":
            print("You went to Oakleigh and Ritza\'s obscenities get you killed by a group of wogs")
        elif choice3 == "maccas":
            print("The icecream machine was not working and Abhi got so annoyed that he you for feet pics to make him feel better. You commit suicide out of shame.")
        else:
            print("You chose a terrible option and had to listen to Mihir talk about L F1 takes. Abhi came and drove you home out of sympathy and you cried yourself to sleep")
    else:
        print("After listening to Kuvindu drone on about kpop for so long, your eardrums burst and you die of resulting blood loss.")
else:
    print("Realising that you watched the less exciting show, you had to endure a lecture from Asvinth about how good JJK is, and died from cringe.")

