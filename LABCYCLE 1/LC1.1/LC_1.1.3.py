#Square of N numbers

list=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    list.append(int(input("Enter the numbers: ")))
print("Square of Numbers: ")
for i in list:
    print(i*i,end=" ")
print(" ")