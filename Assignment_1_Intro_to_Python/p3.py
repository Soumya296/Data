def Leap_Year(year):

    if(year%400==0):
        print("This is a leap year\n")
    elif(year%4==0 and year%100 != 0):
        print("This is a leap year\n")
    else:
        print("This is not a leap year\n")

year = int(input("\nEnter the year: "))
Leap_Year(year)