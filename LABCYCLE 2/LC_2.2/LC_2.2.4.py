#Factors

def factor(x):
    print("The factors of number ",x,'are')
    for i in range(1,x+1):
        if x%i==0:
            print(i)

num=int(input("Enter a number: "))
factor(num)