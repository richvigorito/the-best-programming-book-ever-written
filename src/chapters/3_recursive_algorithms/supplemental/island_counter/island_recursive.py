def get_islands(grid):
    def walk(r, c , grid, current_island, existing_island_cordinates):
           
        if((r, c) in existing_island_cordinates or r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or int(grid[r][c]) == 0):
            ## am i in an existing island cordinate already? ok doesnt count
            ## am out of bounds, ie water? ok cannot walk
            ## am in in water? id grid[r][c] == 0? ... ok cannot walk
            return current_island
        existing_island_cordinates.append((r,c))
        current_island.append((r,c))
        walk(r, c + 1, grid, current_island, existing_island_cordinates)
        walk(r, c - 1, grid, current_island, existing_island_cordinates)
        walk(r + 1, c, grid, current_island, existing_island_cordinates)
        walk(r - 1, c, grid, current_island, existing_island_cordinates)
        return current_island  


    islands = [];
    existing_island_cordinates = [];

    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            island = walk(r, c, grid,[], existing_island_cordinates)
            if (len(island)):
                islands.append(island)
    
    return islands
