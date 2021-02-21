#Factorial of a number

num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial not found for negative numbers!")
elif num==0:
    print("Factorial of",num,"is: ",factorial)
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("Factorial of",num,"is: ",factorial)