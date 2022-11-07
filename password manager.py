master_pwd=input("What is your master password? ")

def view():
    with open ('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw =data.split("|")
            print ("user: ", user, "| password:" , passw)

def add():
    name=input('Enter the account name: ')
    pwd=input("Enter the password: ")
    
    with open("password.txt", 'a') as f:
        f.write( name + "|" + pwd + "\n")

while True:
    mode=input("Would you like to add new password or view existing one (view/add)? ").lower()
    if mode== "q":
     break
    
    if mode=="view":
        view()
    elif mode=="add":
         add()
    else:
        print('Invaild Mood !')
        continue
    