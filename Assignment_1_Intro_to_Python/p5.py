print("\n\nEnter two integers...\n")
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

print("\nPrinting the integers before swapping in the order... " ,x,y)
x,y = y,x
print("\nPrinting the integers after swapping in the order... " ,x,y,end="\n\n")