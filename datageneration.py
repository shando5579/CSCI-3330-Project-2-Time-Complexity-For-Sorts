import random

newnum = range(1, 1000)
#populates array of 1000
def defaultdata():

    neutraldata10 = random.choices(newnum, k = 10)
    print(neutraldata10)

    neutraldata100 = random.choices(newnum, k = 100)
    print(neutraldata100)

    neutraldata1000 = random.choices(newnum, k = 1000)
    print(neutraldata1000)

    #ordered data
    ordereddata10 = list(range(1, 10))
    print(ordereddata10)
    
    ordereddata100 = list(range(1, 100))
    print(ordereddata100)
    
    ordereddata1000 = list(range(1, 1000))
    print(ordereddata1000)

    #Reversed array
    reversedata10 = list(range(1, 10))
    reversedata10.reverse()
    print(reversedata10)

    reversedata100 = list(range(1, 100))
    reversedata100.reverse()
    print(reversedata100)

    reversedata1000 = list(range(1, 1000))
    reversedata1000.reverse()
    print(reversedata1000)
    
defaultdata()

