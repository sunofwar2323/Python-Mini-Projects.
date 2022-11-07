import random

U_win = 0
C_win = 0
try_given = 0
draw = 0

option = ["rock", "paper", "scissors"]

while True:
    try_given += 1
    user_input = input("Chose any: rock paper scissors or q to quit: ").lower()
    if user_input.lower() == "q":
        print("You are out of the game")
        break
    elif user_input not in option:
        print("Your input is not in option.")
        print("Try again")
        continue

    rand_num = random.randint(0, 2)
    computer_pick = option[rand_num]

    print(f'Computer picked is: {computer_pick}')

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        U_win += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("Both picked same !")
        draw += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        U_win += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Both picked same")
        draw += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        U_win += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Both picked same")
        draw += 1
    else:
        print("Computer won")
        C_win += 1

print(f" You played {try_given} times")
print(f" You won  {U_win} times")
print(f" Computer won {C_win} times")
print(f"Both picked same for {draw} times")
print("Thank you ")
