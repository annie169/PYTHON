#add 'ing' at end of a string

def fun_ing(str1):
    if(len(str1)>=3):
        if(str[-3:]=='ing'):
            str1=str1+'ly'
        else:
            str1=str1+'ing'
    print('Modified string is ',str1)
str=input("Enter a string: ")
fun_ing(str)