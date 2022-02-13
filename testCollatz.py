

def collatz(num): #Define a function that passes variable of type integer
    while num != 1: #Do the below steps as long until it doesnt reach 1
        print(num) #print out the num variable value
        if num % 2 == 0: #If the num variable value is even so divide by 2
            num = int(num / 2)
        else:
            num = int(3 * num + 1)  #Otherwise the num variable value is odd so divide by 2
    else:
        print(num) #if the number variable reaches 1 end while
        print('Done!')


def main():
    n = int(input('Please Input a positive integer: ')) # Define a function that takes absolute integer from user and retuns that integer to defined collatz function.
    num =abs(n)
    collatz(num)
main()