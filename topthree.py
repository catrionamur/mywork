# This program generates 10 random numbers.
# prints them out, then
# prints out the top 3
# I will use a list to store and
# manipulate the numbers
import random
# I programming the general case
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100
numbers = []
for i in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeto))
print ("{} random numbers\t {}".format(howMany,numbers))
# I am keeping the original list maybe I don't need to
# I got the idea to sort and split the list from stackover flow
# https://stackoverflow.com/q/32296887

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))