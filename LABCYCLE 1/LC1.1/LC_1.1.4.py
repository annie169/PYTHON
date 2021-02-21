#Vowels in list

list=[]
vowels=['a','e','i','o','u']
string=input("Enter a word: ")
for i in string:
    if((i in vowels)and(i not in list)):
        list.append(i)
print("Vowels present in", string ,'is',list)