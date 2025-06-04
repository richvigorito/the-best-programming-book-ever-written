#import unittest

def get_islands(grid):

    rows, cols = len(grid), len(grid[0])
    existing_island_cordinates = set()
    islands = []

    for r in range(rows):
        for c in range(cols):
            if int(grid[r][c]) == 1 and (r, c) not in existing_island_cordinates:
                island = []
                stack = [(r, c)]

                while stack:
                    cur_row, cur_col = stack.pop()
                    if (
                        0 <= cur_row < rows and 0 <= cur_col < cols and
                        int(grid[cur_row][cur_col]) == 1 and (cur_row, cur_col) not in existing_island_cordinates
                    ):
                        existing_island_cordinates.add((cur_row, cur_col))
                        ## push neigbhoring cords onto stack for consideration
                        island.append((cur_row, cur_col))
                        stack.append((cur_row + 1, cur_col))
                        stack.append((cur_row - 1, cur_col))
                        stack.append((cur_row, cur_col + 1))
                        stack.append((cur_row, cur_col - 1))

                islands.append(island)

    return islands
"""
def data_provider():
    return [
        ([     
            ["1","1","0","0","1"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 4), 
        ([     
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"]
        ], 5), 
        ([     
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]
        ], 1), 
        ([ 
            ["1", "1", "0"],
            ["1", "1", "0"],
            ["0", "0", "0"]
        ], 1),
        ([
            ["1", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "1"]
        ], 2),
        ([
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"]
        ], 5),  
        ([
            ["1", "0", "1"],
            ["0", "0", "0"],
            ["1", "0", "1"]
        ], 4),
        ([
            ["0", "0", "0", "0", "0"],
            ["0", "1", "1", "1", "0"],
            ["0", "1", "1", "1", "0"],
            ["0", "0", "0", "0", "0"]
        ], 1),
        ([
            ["0", "0"],
            ["0", "0"]
        ], 0),
        ([
            ["1", "1"],
            ["1", "1"]
        ], 1),
        ([
            ["1", "1", "0", "0", "1", "1"]
        ], 2),
    ]

class TestNumIslands(unittest.TestCase):
    def test_island_counts(self):
        for i, (grid, expected) in enumerate(data_provider()):
            with self.subTest(f"Test case {i+1}"):
                islands = get_islands(grid)
                print(f"grid: {grid}\nislands: {islands}")
                print(f"island count: {len(islands)} | assert count: {expected}")
                print("")
                self.assertEqual(len(islands), expected)


if __name__ == "__main__":
    unittest.main()
"""
