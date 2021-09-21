import pdb
x=float(input("length "))
y=float(input("width "))
z=float(input("height "))
noPaint=float(input("area with no paint "))
coats=int(input("coats "))
oneCoat=x*y+2*y*z+2*z*x-noPaint
print(coats*oneCoat)