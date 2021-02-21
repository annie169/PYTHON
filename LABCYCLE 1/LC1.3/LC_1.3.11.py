#GCD of two numbers

def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
num=gcd(x,y)
print("GCD of two numbers is: ",num)