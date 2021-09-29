temp=input("do you have a temperature? ")
if temp=="yes":
    throat=input("do you have a sore throat?")
    if throat=="yes":
        print("you have a thoat infection")
    #endif
    else:
        cough=input("do you have a cough?")
        if cough=="yes":
            print("you have a chest infection")
        #endif
    #endelse
#endif
else:
    print("no probs")
#endelse