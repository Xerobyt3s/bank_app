import sqlite3
import hashlib
import socket
import threading

#creates a socket for wireless data transfer, note that all date will need to be encoded to be sent
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 433)) #Change to localhost if you dont want to use my server for authentication

server.listen

def ClientHandeling(c):
    NewOrOld = c.recv(1024).decode()

    if NewOrOld == "old":
        #recives the user data
        c.send("Account name: ".encode())
        AccountName = c.recv(1024).decode()
        c.send("Password: ".encode())
        Password = c.recv(1024)

        Password = hashlib.sha256(Password).hexdigest() #converts password to hash for camparisin against the database

        #connects to the database
        cx = sqlite3.connect("accountData.db")
        cu = cx.cursor()

        #compares your input agaist the database
        cu.execute("SELECT * FROM accountData WHERE AccountName = ? AND Password = ?", (AccountName, Password))
        if cu.fetchall():
            c.send("Authentication complete, have plesent stay!".encode())
            #placeholder for account actions
        else:
            c.send("Authentication failed, please typ again".encode())
    elif NewOrOld == "new":
        #recives the user data for the new account
        c.send("New account name: ".encode())
        NewAccountName = c.recv(1024).decode()
        c.send("New password: ".encode())
        NewPassword = c.recv(1024)

        NewPassword = hashlib.sha256(NewPassword).hexdigest() #converts password to hash so that no plain text version is stored

        #connects to the database
        cx = sqlite3.connect("accountData.db")
        cu = cx.cursor()

        try:
            cu.execute("INSERT INTO AccountData (AccountName, Password) VALUES (?, ?)", (NewAccountName, NewPassword))

            cx.commit()

            c.send("Account created, please proceed to the login page".encode())
        except:
            c.send("Account creation failed, please try again".encode())


while True:
    server.listen()
    client, addr = server.accept()
    threading.Thread(target=ClientHandeling, args=(client,)).start()
    