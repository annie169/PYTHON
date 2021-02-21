#POSITIVE LIST OF NUMBERS

list=[]
n=int(input('Enter the number of elements in list: '))
for i in range(0,n):
    list.append(int(input("enter the integers: ")))
print("Positive integers...")
for i in list:
    if(i>0):
        print(i,end=" ")
print(" ")