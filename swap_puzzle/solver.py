from grid import Grid
from copy import copy, deepcopy

class Solver(): 
    """
    A solver class, to be implemented.
    """
    
    def solveCell(self, cell):
        i,j = cell
        value = self.state[i][j]

        if i != 0 and self.state[i-1][j] < value:
            grid.swap(cell1, (i-1, j))
        
        if j != 0 and self.state[i][j-1] < value:
            grid.swap(cell1, (i, j-1))
        

        


    def get_solution(self, gridToSolve):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """

        stateCopy = deepcopy(gridToSolve)
        while(not grid.is_sorted(stateCopy)):
            for i in range(gridToSolve.m): #We go through the array 
                for j in range(gridToSolve.n):
                    solveCell(self, (i,j))


        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

