import random

list = []

for x in range(0,20):
    list.append(random.randint(0,1000))

print("\nPrinting total list: \n", list[:],end="\n\n")
print("\nPrinting after 5th index: (Excluding 5th index)\n", list[6:],end="\n\n")
print("\nPrinting before 6th index: (Excluding 6th index)\n", list[:6],end="\n\n")
print("\nPrinting between 2nd and 8th index: (Including 2nd and 8th) \n", list[2:9],end="\n\n")
