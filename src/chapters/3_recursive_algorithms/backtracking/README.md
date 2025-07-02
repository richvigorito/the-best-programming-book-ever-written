# 🔁 Backtracking Algorithms

> 📖 Section 3.4 – *Algorithms + Data Structures = Programs*  
> Niklaus Wirth, Page 137–140

---

Backtracking is a **recursive problem-solving technique** that tries to build solutions incrementally, **abandoning partial paths** as soon as it's clear they won’t lead to a valid outcome.

It is especially useful in problems like:
- The Knight’s Tour
- The Eight Queens Problem
- Sudoku solvers
- Maze solvers
- Combinatorics / constraint satisfaction

---

## 🌲 How It Works

A backtracking algorithm typically explores a **tree of choices**, and follows this general structure:

```pascal
PROCEDURE Try;
BEGIN
  IF solution incomplete THEN
    initialize selection of candidates;
    WHILE ~(no more candidates) AND ~CanBeDone(candidate) DO
      select next candidate
    END
  END
END Try;

PROCEDURE CanBeDone(candidate): BOOLEAN;
BEGIN
  record move;
  Try;
  IF not successful THEN
    undo move
  END;
  RETURN successful
END CanBeDone;
```

---
📚 Subsections
♞ Knight's Tour
Goal: Visit every square on an n x n chessboard exactly once with a knight.

Backtracking Variant: Single solution

Reference: Wirth, p. 137–141

---
👑 Eight Queens
Goal: Place 8 queens on a board so none attack each other.

Backtracking Variant: Find all valid solutions

Reference: Wirth, p. 141–147
