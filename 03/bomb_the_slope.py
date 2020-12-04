def bomb_the_slope(grid, x, y):

    # how wide is the grid?
    width = len(grid[0])
    length = len(grid)

    # start in the top left square of the grid
    run = 1

    count = 0

    for i in range(y, length, y):
        
        run += x
        if run > width:
            run = run - width

        char = grid[i][run-1]
        if char == '#':
            count += 1

    return count