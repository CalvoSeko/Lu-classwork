import random
play = input("Do you want to play? (y/n)" )### SRC - Okay, but I wanted an Yes/No answer...
count=0
while play == "y": ### SRC - If you know how many rounds there are use a for loop.
    print("0 rock, 1 paper, 2 scissors")
    print("guess:", end=" ")
    guess = int(input())
    print("guessed ", guess)
    computer_guess = random.randint(0,2)
    print("computer guessed", computer_guess)
    situations = [[0,2,1], [1,0,2], [2,1,0], [3,3,3]] ### SRC - This is good, but there's an easier way with MOD
    index = situations[guess][computer_guess]
    outputs = ["tie", "You win", "the computer wins"]
    result = outputs[index]
    count+=1
    print(result)
    print()
    play = input("Do you want to play? (y/n)")
#end while
