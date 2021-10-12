import random
import os, time
game_list=['Rock','Paper','Scissors']
computer=c=0
command=p=0
def clear():
    name = os.name
    # for windows
    if name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')
clear()
x="""\033[1;32;40m\n                                                                                                                                                                                                  
╔═══╗╔═══╗╔═══╗╔╗╔═╗    ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗    ╔═══╗╔═══╗╔══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗
║╔═╗║║╔═╗║║╔═╗║║║║╔╝    ║╔═╗║║╔═╗║║╔═╗║║╔══╝║╔═╗║    ║╔═╗║║╔═╗║╚╣╠╝║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║
║╚═╝║║║ ║║║║ ╚╝║╚╝╝     ║╚═╝║║║ ║║║╚═╝║║╚══╗║╚═╝║    ║╚══╗║║ ╚╝ ║║ ║╚══╗║╚══╗║║ ║║║╚═╝║║╚══╗
║╔╗╔╝║║ ║║║║ ╔╗║╔╗║     ║╔══╝║╚═╝║║╔══╝║╔══╝║╔╗╔╝    ╚══╗║║║ ╔╗ ║║ ╚══╗║╚══╗║║║ ║║║╔╗╔╝╚══╗║
║║║╚╗║╚═╝║║╚═╝║║║║╚╗    ║║   ║╔═╗║║║   ║╚══╗║║║╚╗    ║╚═╝║║╚═╝║╔╣╠╗║╚═╝║║╚═╝║║╚═╝║║║║╚╗║╚═╝║
╚╝╚═╝╚═══╝╚═══╝╚╝╚═╝    ╚╝   ╚╝ ╚╝╚╝   ╚═══╝╚╝╚═╝    ╚═══╝╚═══╝╚══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝╚═══╝
"""
y=0
while y <=len(x):
    os.system('cls')
    print (x[:y])
    time.sleep(.01)
    y=y+1


run=True
while run:
    computer_choice= random.choice(game_list)
    command=input("\033[1;34;40m\nRock, Paper, Scissors or Quit: ")
    if command == computer_choice:
        print("Tie")
    elif command == 'Rock':
        if computer_choice== 'Scissors':
             print('Player Won!')
             p+=1
             print("Player: " +command)
             print("Computer: "+computer_choice)
             print("")
        else:
            print("Computer Won!")
            c+=1
            print("Player: " +command)
            print("Computer: "+computer_choice)
            print("")
    elif command=='Paper':
        if computer_choice =='Rock':
            print('Player Won')
            p+=1
            print("Player: " +command)
            print("Computer: "+computer_choice)
            print("")
        else:
            print("Computer Won")
            c+=1
            print("Player: " +command)
            print("Computer: "+computer_choice)
            print("")
    elif command=='Scissors':
        if computer_choice=='Paper':
            print('Player Won')
            p+=1
            print("Player: " +command)
            print("Computer: "+computer_choice)
            print("")
        else:
            print("Computer Won")
            c+=1
            print("Player: " +command)
            print("Computer: "+computer_choice)
            print("")
    elif command=='Quit':
           break
    else:
        print('\033[1;31;40m\nWrong Command')
print("Player: " +command)
print("Computer: "+computer_choice)
print("")
print("\033[1;31;40m\nScore: Computer: " + str(c) + "  PLayer: " + str(p))
print("")

