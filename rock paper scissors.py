import random
print("Enter 'R' for Rock")
print("Enter 'P' for Paper")
print("Enter 'S' for Scissors")
print("Enter 'Q' for exit")
LIST = ["R", "P", "S"]
count = 0
while True:
    ur = input("Your turn: ")
    op = random.choice(LIST);
    print(ur)
    print("Opponent turn:", op)
    if ur == op:
        print("Dead heat!")
    elif (ur == "R" and op == "S") or (ur == "S" and op == "P") or (ur == "P" and op == "R"):
        print("You win! +1")
        count += 1
    elif (ur == "S" and op == "R") or (ur == "P" and op == "S") or (ur == "R" and op == "P"):
        print("You lose!")
    elif ur == "Q":
        break
    else:
        print("Error!")
print("Your score: ", count)