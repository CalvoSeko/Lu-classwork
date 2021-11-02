def getPword(attempt):
    if attempt == 1:
        password = input("Enter password: ")
        while len(password)<6 or len(password)>8:
            print("Error, Password must be 6 to 8 characters long")
            password = input("Enter password: ")
        return password
        #endif
    if attempt == 2:
        password = input("Enter password again: ")
        return password
    #endif
#endfunction
p1 = getPword(1)
p2 = getPword(2)
while p1 != p2:
    print("Error - password does not match")
    p1 = getPword(1)
    p2 = getPword(2)
#endwhile
print("Password change successful")
    