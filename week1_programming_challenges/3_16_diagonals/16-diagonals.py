def check_up(grid,index,n):
    up_ele = grid[index - n]
    if up_ele != '_':
        return grid[index] == up_ele
    else:
        return True

def check_up_left(grid, index, n):
    up_left_ele = grid[index - (n + 1)]
    if up_left_ele != '_':
        return grid[index] != up_left_ele
    else:
        return True

def check_up_right(grid, index, n):
    up_right_ele = grid[index - (n - 1)]
    if up_right_ele != '_':
        return grid[index] != up_right_ele
    else:
        return True

def check_left(grid, index):
    left_ele = grid[index - 1]
    if left_ele != '_':
        return grid[index] == left_ele 
    else:
        return True

def check_if_conflict_does_not_exist(grid, n):
    index = len(grid) - 1        
    if len(grid) == 1 or grid[index] == '_':
        return True
    if int(index / n) != 0:    
        if index % n == 0:
            if grid[index] == '/':
                return check_up(grid, index, n) and check_up_right(grid, index, n)
            else:
                return check_up(grid, index, n)
        elif index % n  == (n - 1):
            if grid[index] == '/':
                return (check_up(grid, index, n) and check_left(grid, index))
            else:
                return (check_up(grid, index, n) and check_up_left(grid, index, n) and check_left(grid, index))
        elif 0 < index % n < (n - 1):
            if grid[index] == '/':
                return (check_up(grid, index, n) and check_up_right(grid, index, n) and check_left(grid, index))
            else:
                return (check_up(grid, index, n) and check_up_left(grid, index, n) and check_left(grid, index))
    else:
        return check_left(grid, index)
    

def extend_grid(grid, n, m):
    if len(grid) == n * n:
        if grid.count("/") + grid.count("\\") == m:
            print(grid)
            for i in range(n):
                grid_str = ''
                for j in range(n):
                    grid_str += grid[n * i + j]
                print(grid_str)
            return
        else:
            return

    for k in ['/', '\\', '_']:
        grid.append(k)
        if check_if_conflict_does_not_exist(grid, n):
            extend_grid(grid, n, m)
        grid.pop()

extend_grid([], 4, 10)