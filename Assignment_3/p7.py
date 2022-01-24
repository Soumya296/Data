import pandas as pd
import random

#-------------------------read the dataset-----------------------------
data = pd.read_csv('Salary_Data.csv')
print("\nReading the dataset \n")
print(data)

#------------------------counting the rows and colums--------------------------
rows = len(data.axes[0])
cols = len(data.axes[1])

print("\nThis data set has %d rows and %d columns\n"%(rows, cols))

#----------------------printing first 5 entries---------------

print("Printing the first 5 rows\n",data.head(5))

#---------------------summary of numerical cols-------------------

print("\nPrinting summary of the numerical colums...\n")
print(data.describe())

#--------------------------randomly select subset of dataset---------------------

subset = random.randint(5,rows)
print("\nPrinting randomly selected subset of the salary dataset with %d rows \n"%subset)
print(data.sample(subset))