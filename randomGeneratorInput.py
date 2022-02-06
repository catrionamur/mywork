# randomGeneratorInput
# This program takes from user 10 numbers and output a random number from the list of numbers
# author: Catriona Murray
import random
import numpy as np #NumPy is a Python library used for working with arrays
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
fourth = int(input("Enter fourth number: "))
fifth = int(input("Enter fifth number: "))
sixth = int(input("Enter sixth number: "))
seventh = int(input("Enter seventh number: "))
eight = int(input("Enter eight number: "))
ninth = int(input("Enter ninth number: "))
tenth = int(input("Enter tenth number: "))

numberList = [first,second,third,fourth,fifth, sixth, seventh,eight,ninth,tenth]
print("here is a random number {} ",np.random.choice(numberList, size=1, replace=False)) # numpy.random.choice() function is used to get random elements from a NumPy array
# size signifies the number of rows in the array, in this case its a 1d array 