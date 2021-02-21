#Replace first letter with '$'

def stringreplace(str1):
    firstchar=str1[0]
    str2=str1[1:].replace(firstchar,'$')
    print(firstchar + str2)
str1=input("Enter a string: ")
stringreplace(str1)