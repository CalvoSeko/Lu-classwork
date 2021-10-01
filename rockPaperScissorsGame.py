import random
rounds=int(input("How many rounds do you want to go? "))
count=0
while count!=rounds:
    print("0 rock, 1 paper, 2 scissors")
    print("guess:", end=" ")
    guess = int(input())
    print("guessed ", guess)
    computer_guess = random.randint(0,2)
    print("computer guessed", computer_guess)
    situations = [[0,2,1], [1,0,2], [2,1,0], [3,3,3]]
    index = situations[guess][computer_guess]
    result_messages = ["tie", "You win", "the computer wins"]
    result = result_messages[index]
    count+=1
    print(result)
    print()
