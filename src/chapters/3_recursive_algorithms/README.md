# Chapter 3 – Recursive Algorithms

## Overview

Chapter 3 explores **recursive algorithms**, beginning with the conceptual definition of recursion as a self-referential structure found not only in mathematics but in daily life. Old school "TV picture" visual, where an image recursively includes itself was a nice touch.

<p align="center">
  <img src="/assets/recursion_tv.png" alt="Recursion" width="400"/>
</p>



The chapter presents recursion as a solutions for problems that are defined recursively, such as:

- Natural numbers
- Tree structures
- The factorial function

Wirth discusses the general recursive form: A formula that refines itself with termination conditions to ensure recursion eventually halts. 

## Key Concepts

- **Recursive Definitions**: Finite statements that define infinite sets.
- **Direct vs Indirect Recursion**: A procedure calling itself vs calling another that leads back to it.
- **Scope and Local Variables**: Each recursive call has its own environment.
- **Termination**: Ensuring recursion ends, often by using a decreasing value like `n-1`.

## When *Not* to Use Recursion

Wirth gives several reasons and patterns where recursion is inappropriate:

- When recursive calls lead to exponential growth in function calls.
- When recursion causes deep call stacks and inefficiency.
- If the problem follows simple iterative patterns (e.g., factorial, Fibonacci). Which is funny since Fibonacci is the poster child for recursion. run ``fact_test.py`` to clock both approaches.  


