import numpy
import time

SIZE = int(input("Choose the grid size: "))

def dead_state():
    return numpy.zeros((SIZE, SIZE), dtype = int)

def random_state():
    return numpy.random.randint(0, 2, size = (SIZE, SIZE))

def render(board):
    print('-' * SIZE)
    for x in board:
        for y in x:
            print('#' if y == 1 else ' ', end = '')
        print()
    print('-' * SIZE)
        
def next_board_state(initial_state):
    new_state = dead_state()
    for x in range(SIZE):
        for y in range(SIZE):
            if(x == 0 and y == 0):
                sum = initial_state[x][y+1] + initial_state[x+1][y] + initial_state[x+1][y+1]
            elif(x == SIZE - 1 and y == 0):
                sum = initial_state[x][y+1] + initial_state[x-1][y] + initial_state[x-1][y+1]
            elif(x == 0 and y == SIZE - 1):
                sum = initial_state[x][y-1] + initial_state[x+1][y] + initial_state[x+1][y-1]
            elif(x == SIZE - 1 and y == SIZE - 1):
                sum = initial_state[x][y-1] + initial_state[x-1][y] + initial_state[x-1][y-1]
            elif(x == 0):
                sum = initial_state[x][y-1] + initial_state[x][y+1] + initial_state[x+1][y-1] + initial_state[x+1][y] + initial_state[x+1][y+1]
            elif(x == SIZE - 1):
                sum = initial_state[x][y-1] + initial_state[x][y+1] + initial_state[x-1][y-1] + initial_state[x-1][y] + initial_state[x-1][y+1]
            elif(y == 0):
                sum = initial_state[x-1][y] + initial_state[x+1][y] + initial_state[x-1][y+1] + initial_state[x][y+1] + initial_state[x+1][y+1]
            elif(y == SIZE - 1):
                sum = initial_state[x-1][y] + initial_state[x+1][y] + initial_state[x-1][y-1] + initial_state[x][y-1] + initial_state[x+1][y-1]
            else:  
                sum = initial_state[x][y-1] + initial_state[x][y+1] + \
                    + initial_state[x-1][y] + initial_state[x+1][y] + \
                    + initial_state[x-1][y-1] + initial_state[x-1][y+1] \
                    + initial_state[x+1][y-1] + initial_state[x+1][y+1]

            if initial_state[x][y] == 1:
                if sum < 2 or sum > 3:
                    new_state[x][y] = 0
                else:
                    new_state[x][y] = 1
            else:
                if sum == 3:
                    new_state[x][y] = 1
    
    return new_state

def main():
    initial_state = random_state()
    while(True):
        render(initial_state)
        initial_state = next_board_state(initial_state)
        time.sleep(.5)
    
if __name__ == '__main__':
    main()