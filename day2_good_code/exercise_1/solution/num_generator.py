from numpy import random

def num_generator(seedNum=random.randint(100),numRand=50,maxNum=100):

    random.seed(seedNum)
    output =random.randint(100, size=(numRand))

    return list(output)

def do_nothing():
    print("I do nothing")