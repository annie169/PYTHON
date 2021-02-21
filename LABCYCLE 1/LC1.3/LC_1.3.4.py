#Print extension of file

filename=input("enter filename ")
extn=filename.split(".")
print('the extension of the file is: '+repr(extn[-1]))