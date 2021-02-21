#Lambda function to find area

square=lambda x:x*x
rectangle=lambda x,y:x*y
triangle=lambda x,y:0.5*x*y
print("Area of square: ",square(4))
print("Area of rectangle: ",rectangle(4,5))
print("Area of triangle: ",triangle(4,5))