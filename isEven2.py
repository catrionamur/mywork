# isEven2.py
# This program takes in input from a user, checks for an even number and asks for user input until -1 is reached
# author: Catriona Murray
guessLimit = -1 #Threshold for breaking loop
guess = int(input("Please guess the number:")) #Take in user input as int.
while guess != guessLimit: # do the below activities while the number entered is not = -1
    if (guess % 2) == 0:  # if the number entered is even print out that its an even number
        print ("{} is an even number".format(guess))
    else:
        print("{} is an odd number".format(guess)) #if the number is odd then print out even number
    guess = int(input("enter another integer:"))

print("Well done! Yes the number was ", guessLimit) #if the number -1 is entered end the while loop.  I had it an issue where the loop was endless this was because of indentation so now understand importance of indenting in python