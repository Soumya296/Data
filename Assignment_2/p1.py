'''

Soumyadip Payra
CSE A
197178

'''

import random
#--------------initializing list with different variable types---------------

my_list = [2,3.5,50000000000000000,'c',"soumya",5.7,21,(12,25.0,"NITW")]
print("\nPrinting the list\n")
print(my_list)

print("\nDifferent data types in list are...")
for i in my_list:
    print(type(i)," \t",i)

#--------------counting length of the list---------------------

print("\nThe length of the list is ", len(my_list))

#-------------access the last element------------------------

print("\nThe last element of the list is ", my_list[-1])

#-------------add one item using append-------------------

my_list.append("CSE")
print("\nappended list...", end="\t")
print(my_list)

#---------------add multiple items using extend-------------

my_list.extend(("Hello darkness my old friend").split())
print("\nextended list...", end="\t")
print(my_list)

#-------------------indexing at 2, 7, -4-------------------------

print("\nItem at index 2", my_list[2])
print("\nItem at index 7", my_list[7])
print("\nItem at index 4 from ending", my_list[-4])

#---------------insertion at specific index [4]--------------------

my_list.insert(4,71)
print("\nupdated list after insertion...",end="\t")
print(my_list)

#--------------replacing index 2-------------------------

my_list[2] = "Data Science"
print("\nupdated list after replacing index 2...", end="\t")
print(my_list)

#-----------------adding duplicate element----------------

i = random.randint(0,len(my_list))
my_list.append(my_list[i])
print("\nupdated list after appending duplicate random item :", my_list[i]," from index ", i, "\n")
print(my_list)

#-----------------removing item from index 4--------------------

my_list.pop(4)
print("\nprinting list after poping element at index 4 : ", end="\t")
print(my_list)

#----------------sorting ascending-------------------

numerical_list = [random.randint(0,9999) for i in range(1,20)]
print("\nPrinting the Numerical list\n")
print(numerical_list,end="\n\n")
numerical_list.sort()
print("\nPrinting sorted list in ascending order...\n")
print(numerical_list)

# #------------------sorting descending----------------------

numerical_list.sort()
print("\nPrinting sorted list in descending order...\n")
print(numerical_list)

#----------------------reverse------------------

my_list.reverse()
print("\nPrinting list after reversing the order...\n")
print(my_list)





