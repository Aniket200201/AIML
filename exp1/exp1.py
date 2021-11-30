def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print ('\n')

def find_unassigned_location(grid, l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

def used_in_row(grid, row, num):
    for i in range(9):
        if(grid[row][i] == num):
            return True
    return False

def used_in_col(grid, col, num):
    for i in range(9):
        if(grid[i][col] == num):
            return True
    return False

def used_in_box(grid, row, col, num):
    start_row = row - row%3
    start_col = col - col%3
    for i in range(3):
        for j in range(3):
            if(grid[i + start_row][j + start_col] == num):
                return True
    return False

def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row,col, num)

def solve_sudoku(grid):

     #Here, l is a list which keeps our next unassigned location   
    l =[0, 0]
     
    # If there is no unassigned location,then we return True  
    if(not find_unassigned_location(grid, l)):
        return True
     
    #Get the row number and column number of next unassigned location
    row = l[0]
    col = l[1]
     
    # consider digits 1 to 9
    for num in range(1, 10):
        if(is_safe(grid,row, col, num)):
            grid[row][col]= num
            if(solve_sudoku(grid)):
                return True
            grid[row][col] = 0       
    return False

grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
          
#Define our grid
grid = []

print("Enter the grid:")
for i in range(1,10):
    row = list(map(int, input("Enter your next row: ").strip().split()))
    grid.append(row)

#for i in range(9):          
    #row_i = []
    #for j in range(9):      
         #row_i.append(int(input()))
    #grid.append(row_i)

if(solve_sudoku(grid)):
    print_grid(grid)
else:
    print("No solution")