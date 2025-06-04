import time
import copy
from grids import data_provider
from island_recursive import get_islands as recurse
from island_iterate import get_islands as iterate

def run_tests():
    test_cases = data_provider()
    for i, (grid, expected) in enumerate(test_cases):
        rec_cnt = len(recurse(grid))
        itr_cnt = len(iterate(grid))
        assert rec_cnt == expected, f"[Recursive] Test {i} failed: got {rec_cnt}, expected {expected}"
        assert itr_cnt == expected, f"[Iterative] Test {i} failed: got {itr_cnt}, expected {expected}"
    print("All test cases passed!")

def benchmark(fn, name, executions):
    test_cases = data_provider()
    start = time.time()
    for _ in range(executions):
        for grid, expected in test_cases:
            len(fn( grid))
    end = time.time()
    print(f"{name} took {end - start:.2f} seconds for {executions} for {len(test_cases)} grids, ie {50000 * len(test_cases)} calls")
    

if __name__ == "__main__":
    run_tests()
    execution_cnt = 50000
    print("Benchmarking...")
    benchmark(recurse, "Recursive", execution_cnt)
    benchmark(iterate, "Iterative", execution_cnt)

