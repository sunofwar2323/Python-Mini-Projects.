print("Welcome to my Computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()
print("Okay! Let's play: ")
score=0

answer= input("What does CPU stands for? ")
if answer.lower()== "central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    
answer= input("What does GPU stands for? ")
if answer.upper() == "GRAPHIC PROCESSING UNIT":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    
answer= input("What does RAM stands for? ")
if answer.lower()== "random access memory":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    
answer= input("What does PSU stands for? ")
if answer.lower()== "power supply unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

print('You got ' + str(score) + " answer correct !")
print ("Your final percentage is " + str ((score/4)*100) + "%." )
    
    
    
    