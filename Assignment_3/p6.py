import pandas as pd
import numpy as np

attendance_dict = {

    "monday" : 153,
    "tuesday" : 171,
    "wednesday" : 162,
    "thursday" : 169,
    "friday" : 176,
    "saturday" : 161,
    "sunday" : 123
}

attendance = pd.Series(data = attendance_dict, index = [key for key in attendance_dict.keys()])

#---------------------------------------dataset-----------------------------------------------

print("\nDisplaying the Dataset\n")
print(attendance)

#------------------------------sorting dataset in ascending order-----------------------------

attendance_sorted = attendance.sort_values()
print("\nDisplaying the Dataset after sorting on the attendance\n")
print(attendance_sorted)

#-------------------------------------day with max attendies-----------------------------------

max_day = attendance.index[attendance.argmax()]
max_attendance = attendance.max()
print("\nThe day with the most number of attendance is %s with attendance %d"%(max_day,max_attendance))

#----------------------------------1st 2 days------------------------------------------

print("\nPrinting the first two days and their attendance count: \n")
print(attendance[:2])

#--------------------------plot--------------------------------------

print("\nDrawing the plots and savign as png file as terminal may not support the plot...\n")
attendance.plot().get_figure().savefig("Plot_Attendance_P6.png") #saving the plot as the terminal may not be able to show the output
