#Character Frequency

dict={}
str=input("Enter a string: ")
for n in str:
    key_s=dict.keys()
    if n in key_s:
        dict[n]=dict[n]+1
    else:
        dict[n]=1
print("Character frequency of ",str,"is",dict)