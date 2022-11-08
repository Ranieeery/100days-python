from getpass import *

def login(i):
  while (i < 3):
    username = input("What is your username?: ")
    password = getpass("What is your password? ")
    if username == "Raner" and password == "PyCharm":
      print("Welcome David!")
      break
    else:
      if i == 2:
        print("Access denied. Try again in 30 minutes")
      else: 
        print("That is not the correct username or password. Try again!")
      i += 1
      continue
    
print("REPLIT LOGIN SYSTEM")
login(0)