# Python program to Find day of
# the week for a given date
# Author: Catriona Murray
import calendar
 
def findDay(date): #function that finds the day of the week 
    day, month, year = (int(i) for i in date.split(' '))   
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
    return (days[dayNumber])
datesInput = input("Enter date dd mm yyyy: ") #enter in date 
date = datesInput # assign the input to varoia[]
print(findDay(date)) # Output the day of the weel
if findDay(date) == calendar.SATURDAY or calendar.SUNDAY: # If the day of the week is Sunday or saturay we know its the weekend
    print ("Its the weekend")
else:
    print ("Its a weekday") #Otherwise print out that its a weekday