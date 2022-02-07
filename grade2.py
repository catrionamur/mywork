# This program reads in
# a students percentage
# and prints out the
# corresponding grade taking into account rounding percentages.  Another option is to use ceiling math function to round the values up
percentage = float(input("Enter the percentage: "))
#print (percentage)
if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100") #only take in a valid number
elif percentage < 39.5: # we know it is greater than 0 but has to be less than 39.5 as 39. is rounded up to a passing grade
    print ("Fail")
elif percentage >= 39.5 and percentage < 49.5: # And specifies that if both conditions are true print or otherwise check if the value matches the other conditions
     print ("Pass")
elif percentage >= 49.5 and percentage < 59.5: #between 49.5 and 59.5 for rounding
    print ("Merit1")
elif percentage >= 59.5 and percentage < 69.5: # between 59.5 and and 69.5 for rounding
    print ("Merit2")
else: # the only option left is between 69.5 and 100 
    print ("Distinction")

