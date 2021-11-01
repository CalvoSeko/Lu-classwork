list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
item = 0
for i in range (0,7):
	item = list2[i]
	for j in range (0,11):
			if item > list1[j] and item < list1[j+1]:
				list1.insert(j+1, item)

print(list1)