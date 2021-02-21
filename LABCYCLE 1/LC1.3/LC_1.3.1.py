#Exchange first and last characters

def change(string):
    return string[-1:]+string[1:-1]+string[:1]
string=input("Enter a string:  ")
print("Modified string:  ")
print(change(string))