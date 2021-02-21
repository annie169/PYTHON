#List of integers except even numbers

num=[11,12,13,14,15,16]
print("List of integers: ",num)
for i in num:
    if(i%2==0):
        num.remove(i)
print("List after removing even numbers ",num)