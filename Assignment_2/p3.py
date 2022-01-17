'''

Soumyadip Payra
CSE A
197178

'''

set1 = {22,1,13,19,75,111,53,68,50,17,81,86,99,47}
set2 = {61,1,16,18,71,115,53,63,51,17,89,83,97,46}

print("\nPrinting the set1 :", end="\t")
print(set1)

print("\nPrinting the set2 :", end="\t")
print(set2)

#---------------------union-----------------------------

print("\nTaking union of set1 and set2 :", end="\t")
print(set1.union(set2))

#----------------intersection----------------------

print("\nTaking union of set1 and set2 :", end="\t")
print(set1.intersection(set2))


#-----------------add---------------------

print("\nAdding 89 and 46 to set 1")
set1.add(89)
set1.add(46)
print("\nPrinting the set1 :", end="\t")
print(set1)

print("\nAdding 183 and 43 to set 2")
set2.add(183)
set2.add(43)
print("\nPrinting the set2 :", end="\t")
print(set2)

#-------------------update---------------

list1 = [119,25,237]
list2 = [59,64,824]

set1.update(list1)
set2.update(list2)

print("\nUpdating set 1 with the list1 : ", list1)
print("\nprinting the updated set1 ",set1)

print("\nUpdating set 2 with the list2 : ", list2)
print("\nprinting the updated set2 ",set2)

#------------------------Difference--------------------

print("\nDifference between set1 and set2 : ", set1.difference(set2), end="\n")
print("\nDifference between set2 and set1 : ", set2.difference(set1), end="\n")

#---------------------symmetric set difference------------------

print("\nSymmetric Difference between set1 and set 2 : ", set1.symmetric_difference(set2), end="\n\n")

