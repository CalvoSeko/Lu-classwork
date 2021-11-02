def multiple():
    pupilName = input("What is your name? ")
    table = int(input("Enter times table, start number and end number"))
    startNum = int(input())
    endNum = int(input())
    print("hi "+pupilName+" ... here is your times table")
    for i in range(startNum, endNum+1):
        print (str(table) + " x " + str(i) + " = " + str(table*i))
    #endfor 
#endfunction
multiple()