#12. Write a program that prints the calendar for a given month and year.

#Note : Use 'calendar' module.

import calendar 

month= int(input("Enter the month(1-12) to display calender: "))
year=  int(input("Enter the year to display calender: "))

print(calendar.month(year,month))


