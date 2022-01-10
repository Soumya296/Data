import numpy as np
print("\nEnter the length of the sides of the triangle\n")

x = float(input("Enter the length of the first side: "))
y = float(input("Enter the length of the second side: "))
z = float(input("Enter the length of the third side: "))

s= (x+y+z)/2

area = np.sqrt(s*(s-x)*(s-y)*(s-z))
print("\nThe area of the triangle is: ", area, " sq. units\n\n")