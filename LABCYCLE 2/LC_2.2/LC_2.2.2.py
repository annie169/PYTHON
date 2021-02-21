#Length of longest word

def longest(list2):
    max=len(list2[0])
    temp=list2[0]
    for i in list2:
        if(len(i)>max):
            max=len(i)
            temp=i
    print("word with longest length is ",temp,"length",max)

list1=['Mars','Earth','Venus','Saturn']
longest(list1)