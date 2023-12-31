import socket
import os
import time


Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connects to server through a socket
Client.connect(("localhost", 9999)) #Change to localhost if you dont want to use my server for authentication

MenuSelected = 0

while True:
    #prints the logo for the bank
    print("""                                      
  ,-----.    ,---.  ,--.  ,--.,--. ,--. 
  |  |) /_  /  O  \ |  ,'.|  ||  .'   / 
  |  .-.  \|  .-.  ||  |' '  ||  .   '  
  |  '--' /|  | |  ||  | `   ||  |\   \ 
  `------' `--' `--'`--'  `--'`--' '--' 
                                        """)
    print("_______________________________________\n")

    match MenuSelected:
        case 0:
            print("Welcome to Bank, what can we do for you\n")
            print("1. login to existing account")
            print("2. create new account")
            print("3. exit")
            try:
                MenuSelected = int(input("option: "))
            except:
                MenuSelected = 0

        case 1:
            #selects authentication for existing account and displays info to user
            Client.send("old".encode())
            #asks for account name
            Message = Client.recv(1024).decode()
            Client.send(input(Message).encode())
            #asks for password
            Message = Client.recv(1024).decode()
            Client.send(input(Message).encode())

            Message = Client.recv(1024).decode()
            print(Message)
            time.sleep(2)

            MenuSelected = 0

        case 2:
            #selects creation of new account and displays info to user
            Client.send("new".encode())
            #asks for the new account name
            Message = Client.recv(1024).decode()
            Client.send(input(Message).encode())
            #asks for the new password
            Message = Client.recv(1024).decode()
            Client.send(input(Message).encode())
            
            #confirms if account has been created
            Message = Client.recv(1024).decode()
            print(Message)
            time.sleep(2)
            
            MenuSelected = 0

        case 3:
            os.system("cls")
            break

        case _:
            MenuSelected = 0
        
    #clearing the screen
    os.system("cls")
        
    