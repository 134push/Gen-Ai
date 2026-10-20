## leap year or not 

year = int(input("enter the current year : "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("the year is a leap year : ")
        else:
            print("the current year is not leap year :")
        print("the current year is not leap year :")
else:
     print("the current year is not leap year :")
