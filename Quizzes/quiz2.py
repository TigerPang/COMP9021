# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by *** and Jack for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

nob_of_longest_paths = 0
def get_paths():
    global max_length
    global nob_of_longest_paths
    for i in range(height):
        for j in range(width):
            if i != None:
                if max_length < grid[i][j]:
                    max_length = grid[i][j]
                    nob_of_longest_paths = 1
                elif max_length == grid[i][j]:
                    nob_of_longest_paths += 1
            else:
                max_length = 0
                nob_of_longest_paths = 0
            if i == None and j == None:
                for i in range(height):
                    for j in range(width):
                        if grid[i][j] == 0:
                            nob_of_time = 0
                            get_paths(i, j)
            else:
                if i > 0:
                    if grid[i - 1][j] == grid[i][j] + 1:
                        get_paths(i - 1, j)

                if i < height - 1:
                    if grid[i + 1][j] == grid[i][j] + 1:
                        get_paths(i + 1, j)

                if j > 0:
                    if grid[i][j - 1] == grid[i][j] + 1:
                        get_paths(i, j - 1)

                if j < width - 1:
                    if grid[i][j + 1] == grid[i][j] + 1:
                        get_paths(i, j + 1)
                return max_length, nob_of_longest_paths


    # Replace pass above with your code

    # Insert your code for other functions


try:
    for_seed, max_length, height, width = [int(i) for i in
                                           input('Enter four nonnegative integers: ').split()
                                           ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()

length, a = max_length, nob_of_longest_paths



if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
