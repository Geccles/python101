import random

choiceList = ["Rock", "Paper", "Scissors"]
userName = input("Welcome to rock, paper, scissors shoot game, what's your name? ")

while True:
    userChoice = input("chose rock, paper or scissors ")
    userChoice = userChoice.lower()
    if userChoice == "quit":
        break
    if userChoice.lower() != "rock" and userChoice.lower() != "paper" and userChoice.lower() != "scissors":
        input("Please choose one of the following options, rock, paper or scissors: ")
        continue
    
    compChoice = random.choice(choiceList)
    compChoice = compChoice.lower()
    print(f"Computer chose: {compChoice}")

    if userChoice == compChoice:
        print(f"{userName}, you tied!")
        continue
    elif userChoice == "paper" and compChoice == "rock":
        print(f"{userName}, your {userChoice} beat {compChoice}")
        break
    elif userChoice == "rock" and compChoice == "scissors":
        print(f"{userName}, your {userChoice} beat {compChoice}")
        break
    elif userChoice == "scissors" and compChoice == "paper":
        print(f"{userName}, your {userChoice} beat {compChoice}")
        break
    else:
        print(f"{userName}, sorry you lost to {compChoice}.")
