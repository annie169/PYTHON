from graphics.threedgraphics import cuboid as cb 
from graphics.threedgraphics import sphere as sp 
from graphics import circle as cr 
from graphics import rectangle



r=int(input("enter radius of circle: "))
cr.c_area(r)
cr.c_per(r)

l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
rectangle.r_area(l,b)
rectangle.r_per(l,b)

s=int(input("Enter radius of sphere: "))
sp.sphere_circum(s)
sp.sphere_area(s)

lc=int(input("Enter length of cuboid: "))
wc=int(input("Enter width of cuboid: "))
hc=int(input("Enter height of cuboid: "))
cb.cub_area(lc,wc,hc)
cb.cub_per(lc,wc,hc)


