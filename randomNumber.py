#randomNumber.py
#author: Catriona Murray
# This program randomnly generates a number from 0 to 100 for sample size entered by user
import random
rangeSize = int(input("Please enter the sample size:"))
x = random.sample(range(0,100), rangeSize) #Print out a list of random numbers between 0  t0 100, print out max of 10 numbers https://pythonprogramminglanguage.com/randon-numbers/
print ("Random set of numbers are: ",(x))
