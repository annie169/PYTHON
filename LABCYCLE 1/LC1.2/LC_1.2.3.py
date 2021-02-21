#Occurance of letter 'a'

list=['annu','sonu','megha','jewel']
count=0
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print("Number of 'a' in list is ",count)