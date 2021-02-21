#Form a list of integers, for integers greater than 100 store over

new_list=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    element=int(input("Enter digit: "))
    if element>100:
        new_list.append("Over")
    else:
        new_list.append(element)
print(new_list)