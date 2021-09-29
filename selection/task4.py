type=input("which type of car? ")
sto=False
if type=="Economy car":
    sto=True
#endif
elif type=="Saloon car":
    sto=True
#endif
elif type=="Sports car":
    sto=True
#endif
else:
    sto=False
#endelse
if sto==True:
    print("valid")
    pro=input("proceed or cancel?")
    if pro=="proceed":
        print("Have a nice day.")
    #endif
#endif