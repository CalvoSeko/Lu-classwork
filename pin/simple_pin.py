pin=str(input("insert 4 digit pin "))
list = [] 
count = 0
for i in range(0,4): 
    for j in range(0,4): 
        for k in range(0,4): 
            for l in range(0,4):
            	if i != j and i != k and i != l and i != l and j != k and j != l and k != l:
                	count += 1
                	list.append(1000*int(pin[i])+100*int(pin[j])+10*int(pin[k])+int(pin[l]))
print(count)
print(list)
