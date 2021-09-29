trigger=bool(input("trigger "))
movementGround=bool(input("ground "))
movementFirst=bool(input("first floor "))
if trigger==True:
    if movementFirst or movementGround==True:
        print("intruder alert!")
    #endif
#endif