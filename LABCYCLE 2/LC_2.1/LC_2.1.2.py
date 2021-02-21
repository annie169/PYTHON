#Fibonacci Series

n1=0
n2=1
nterms=int(input("Number of terms: "))
if nterms<=0:
    print("Enter a positive number!")
elif nterms==1:
    print("Fibonacci series upto ",nterms)
    print(n1)
else:
    print("...Fibonacci Series...")
    count=0
    while count<nterms:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
print(" ")