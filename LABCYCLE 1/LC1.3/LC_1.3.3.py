#Biggest of three numbers

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))

if (a>=b)and(a>=c):
    largest=a
elif(b>=a)and(b>=c):
    largest=b
else:
    largest=c
print('The largest among 3 numbers: ',largest)