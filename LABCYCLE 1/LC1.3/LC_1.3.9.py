#Sort dictionary in ascending and descending order

d={'apple':30,'microsoft':20,'IBM':10}
print("List is : ",d)
l_a=list(d.items())
l_a.sort()
print("List in ascending order",l_a)

l_d=list(d.items())
l_d.sort(reverse=True)
print("List in descending order: ",l_d)