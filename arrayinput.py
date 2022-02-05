# arrayInput.py
# This program takes in array of numbers and prints them out
# author: Catriona Murray
from array import * # imports the array library so you can utilize arrays 
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
array_num = array('i', [first,second,third,fourth,fifth, sixth, seventh,eight,ninth,tenth])
for i in array_num:
    print(i)