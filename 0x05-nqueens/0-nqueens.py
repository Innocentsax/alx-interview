#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """
import sys


class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        """ Global Variables """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Checks if k Queen can be placed in i column (True)
        or if the are attacking queens in row or diagonal (False)
        """

        # j checks from 1 to k - 1 (Up to previous queen)
        for j in range(1, k):
            # There is already a queen in column
            # or a queen in same diagonal
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """ Tries to place every queen in the board
        Args:
        k: starting queen from which to evaluate (should be 1)
        """
        # i goes from column 1 to column n (1st column is 1st index)
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in i column
                self.x[k] = i
                if k == self.n:
                    # Placed all 4 Queens (A solution was found)
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    # Need to place more Queens
                    self.nQueen(k + 1)
        return self.res


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for i in res:
    print(i)
