import random
#from array import *
import numpy as np

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

print("here is a random number {} ",np.random.choice(numberList, size=1, replace=False))
