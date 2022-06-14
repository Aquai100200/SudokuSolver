def findNextEmpty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None 

def isValid(puzzle, guess, row, col):
    rowValues = puzzle[row]
    if guess in rowValues:
        return False
   
    colValues = []
    for i in range(9):
        colValues.append(puzzle[i][col])
        
    colValues = [puzzle[i][col] for i in range(9)]
    
    if guess in colValues:
        return False
        

def solveSoduku(puzzle):
    row,col = findNextEmpty(puzzle)
    if row is None:
        return True
    
    for guess in range(1,10):
        if isValid(puzzle, guess, row, col):