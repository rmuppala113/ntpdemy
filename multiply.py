m = int(raw_input("\nEnter value for m: "))
n = int(raw_input("Enter value for n: "))
o = int(raw_input("Enter value for o: "))
p = int(raw_input("Enter value for p: "))

def muti(a,b,c,d):
    global x
    x = a*b*c*d
    print ("\nMultipliction result of {}*{}*{}*{} is:{}".format(m, n, o, p,x))
    expo(x)

def expo(e):
    y = float(e**2)
    z = float(e**e)
    print ("\nSquare root of {}**2 is: {}\n".format(x, y))
    print ("Exponent of {}**{} is: {}\n".format(x,x,z))

muti(m, n, o, p)

