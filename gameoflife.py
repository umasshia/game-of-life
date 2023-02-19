import numpy
import random

def random_state(width, height):
    return numpy.random.randint(0, 2, size = (width, height))

def main():
    print(random_state(10,10))
    
if __name__ == '__main__':
    main()