'''

Soumyadip Payra
CSE A
197178

'''

#------------------intitializing tuple with different data types------------------

my_tuple = (5.8,3,"Soumya",55,(11,22.0,"NITW"),75.5,[25.3,"DSc"],3,3,55)
print("\nPrinting the tuple...\n")
print(my_tuple)

print("\nDifferent data types in tuple are...")
for i in my_tuple:
    print(type(i)," \t",i)

#-------------------------count-----------------------

print("\nNo of times 3 occurs in the tuple ", my_tuple.count(3))
print("\nNo of times 55 occurs in the tuple ", my_tuple.count(55))

#------------------index--------------------

print("\nThe first occurence of 3 in the tuple is at index ", my_tuple.index(3))
print("\nThe first occurence of (11,22.0,'NITW') in the tuple is at index ", my_tuple.index((11,22.0,"NITW")))
