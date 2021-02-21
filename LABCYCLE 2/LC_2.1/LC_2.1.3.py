#Sum

total=0
list1=[]
n=int(input("Enter number of items: "))
for i in range(0,n):
    list1.append(int(input("Enter items: ")))
print("List is: ",list1)
print("Length of list: ",len(list1))
for i in range(0,len(list1)):
    total=total+list1[i]
print("Total sum of list is ",total)