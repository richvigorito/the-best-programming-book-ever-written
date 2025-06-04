# 🏝️ Island Finder — Recursive & Iterative Solutions

So recently I was asked this interview question:

> Given a grid where `0` is water and `1` is land, identify all the land (islands).

I kinda stumbled for like 5 minutes trying to figure it out. My first thought was to do it iteratively, but then I realized recursion actually fits better here. Initially, I thought maybe flattening the grid and doing backtracking would help, but I didn’t get very far with that in the time I had. Even then, I would have ended up doing what I did anyway — which is to treat it as a 2D grid directly. Flattening makes it trickier (even if it might be more efficient), and backtracking doesn’t quite fit since we’re not really “undoing moves” like in 8-queens or similar puzzles.

Eventually, I came up with a recursive solution that worked well enough. Then they asked if I thought recursion was efficient here — I felt that even though I stumbled on both my initial attempt and the iterative approach, the iterative solution probably is more efficient.

So I went ahead and coded both:

1. A recursive version — easier to get right, but a bit tricky under time pressure  
2. An iterative version — a bit more complex to write but faster in practice

I also benchmarked them against the same test cases to see how they compare. Spoiler: iteration wins on speed.

Here’s what I got:

```bash
~/Development/the-best-programming-book-ever-written/src/chapters/3_recursive_algorithms/supplemental/island_counter (main) $ python3 benchmark.py
All test cases passed!
Benchmarking...
Recursive took 3.75 seconds for 50000 for 11 grids, ie 550000 calls
Iterative took 2.78 seconds for 50000 for 11 grids, ie 550000 calls
```
