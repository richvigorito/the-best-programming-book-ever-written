# Pascal’s Triangle
In honor of the programming language Niklaus Wirth created and the language used in the book here is Pascal's Triangle in Pascal. This isnt directly in the book, but Chapter 1 is about fundamental data structures and array's being on of them.d


## What is it?

Pascal’s Triangle is a triangular arrangement of numbers where:

- The outer edges are always 1.
- Each inner value is the sum of the two numbers above it.
- Row n contains the binomial coefficients for (a + b)^n.
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
  1 6 15 20 15 6 1


Example:
Row 4 → 1 4 6 4 1 corresponds to (a + b)^4 = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴.

---

## Arrays and Pascal’s Triangle

In Wirth’s *Algorithms + Data Structures = Programs*, arrays are described as a means of storing related data in indexed positions, allowing direct access by index.

We can think of Pascal’s Triangle as a 2D array `triangle[row, col]` where:

1. **Indexing**:
   - Rows start at index 0 (or 1, depending on the language).
   - Each row contains one more element than the previous row.

2. **Initialization**:
triangle[row, 0] = 1
triangle[row, row] = 1

3. **Computation**:
for col from 1 to row - 1:
triangle[row, col] := triangle[row - 1, col - 1] + triangle[row - 1, col]

4. **Storage Layout**:
In a fixed-size array, you might allocate a maximum size and leave unused cells empty.
Example for n = 5 (unused cells as `_`):

Row 0: 1 _ _ _ _
Row 1: 1 1 _ _ _
Row 2: 1 2 1 _ _
Row 3: 1 3 3 1 _
Row 4: 1 4 6 4 1

---
