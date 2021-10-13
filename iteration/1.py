list = []
clist = []
count = 0
for i in range(5):
    lt = input("input a letter ")
    list.append(ord(lt))
    print(list)
print("max char ", chr(max(list)))
print("min char ", chr(min(list)))