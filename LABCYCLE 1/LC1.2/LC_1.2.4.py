#Check two list are of same length,sum and have any common values

list_a=[1,2,3,4,5,6]
list_b=[6,7,8,9,10,1]
len_a=len(list_a)
len_b=len(list_b)
if len_b==len_a:
    print("List are of same length. ")
else:
    print("List are not of same length.")

total_a=sum(list_a)
total_b=sum(list_b)

if total_b==total_a:
    print("Sums are same.")
else:
    print("Sums are not same.")

output=any(check in list_b for check in list_a)
print("Common value in both list: ",output)
A=set(list_b).intersection(set(list_a))
print("Commom Value: ",A)