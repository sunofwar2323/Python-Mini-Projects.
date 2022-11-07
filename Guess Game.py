import random
top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please enter the number larger than zero.')
        quit()
else:
    print('Please type NUMBER next time')
    quit()

random_number = random.randint(0, top_of_range)
print(f" >>{random_number} ")


guess = 0
while True:
    guess += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter the NUMBER')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are above the correct number!")
    else:
        print("You are below the correct number !")


print("You got it in ", guess, "guesses")
