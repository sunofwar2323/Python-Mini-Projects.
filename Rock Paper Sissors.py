import random

user_wins = 0
computer_wins = 0
try_given = 0
draw = 0

option = ["rock", "paper", "scissors"]

while True:
    try_given += 1
    user_input = input("Enter rock/paper/scissors or q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        print("Your input is not in the option ! ")
        continue

    random_number = random.randint(0, 2)
    #  index 0=rock 1=paper 2=scissors
    computer_pick = option[random_number]
    print("Computer picked : ", computer_pick + " . ")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won !")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("Both picked same , try again!")
        draw += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won !")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Both picked same , try again!")
        draw += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won !")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "scissors":
        print("Both picked same , try again!")
        draw += 1
        continue
    else:
        print("You lost !")
        computer_wins += 1

print("You played ", try_given, "times.")
print("And You won", user_wins, "times.")
print("Computer won ", computer_wins, "times. ")
print("Lastly there was ", draw, "times draw")
print("Thank you ")
