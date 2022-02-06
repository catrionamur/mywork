# convert.py
# This program takes a decimal input as a float, makes negative as a positive and then changes the amount to cents so as to not have rounding error
# author: Catriona Murray
import math #Import math function
number = float(input("Enter a number:")) #Take in a user input as decimal number
absoluteValue = abs(number) #Changes a negative into a positive number
value = int(absoluteValue*100) #Calculate the value in cents so value is multiplied by 100
print('Amount in cents is :',value)