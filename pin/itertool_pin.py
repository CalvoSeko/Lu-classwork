from itertools import permutations 
pin=str(input("introduce 4 digit pin "))
results=permutations(pin)
for i in results:
    print(i)
#end of for loop