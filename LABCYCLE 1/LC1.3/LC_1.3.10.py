#merge two dictionaries

d1={'a':28,'b':30,'c':29}
d2={'d':26,'e':35,'f':27}
d=d1.copy()
d.update(d2)
print(" D1 ",d1)
print(" D2 ",d2)
print("Merged: ",d)