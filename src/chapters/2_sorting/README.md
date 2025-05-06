# Chapter 2 – Sorting

Sorting is a foundational topic in computer science that demonstrates the importance of algorithmic efficiency and data structure choice. Depending on whether you're sorting data stored in memory (arrays) or in external files, the approach and performance considerations differ dramatically.

> The choice of a sorting algorithm often depends on the **structure of the data** and where it's stored—internal memory vs. external storage. The images below from the book illustrate these distinctions clearly:

<p align="center">
  <img src="/assets/array_sorting.png" alt="Array Sorting" width="400"/>
</p>

<p align="center">
  <img src="/assets/file_sorting.png" alt="File Sorting" width="400"/>
</p>

---

## 📐 A Note on Big O Notation

Big O notation describes how an algorithm's **runtime or space requirements grow** as a function of input size. It's a way to **abstract away machine specifics** and focus on algorithm behavior:

| Notation | Name              | Description |
|----------|-------------------|-------------|
| O(1)     | Constant Time     | No dependency on input size. |
| O(log n) | Logarithmic Time  | Input size reduced each step (e.g., binary search). |
| O(n)     | Linear Time       | Time grows directly with input size. |
| O(n²)    | Quadratic Time    | Often seen in naive nested loops, e.g., bubble sort. |
| O(n log n) | Log-linear Time | Optimal time complexity for many sorts. |

---

## 🔢 Arry Sorting Algorithms

This chapter contains implementations of various sorting algorithms. Each subfolder contains code (in both Pascal and Python) and an explanation of how the algorithm works.

### 📂 [Insertion Sort](./array/insertion_sort)
- **Big O (Best):** O(n)
- **Big O (Average/Worst):** O(n²)
- **Description:** Builds the sorted array one item at a time by comparing each new element to the ones already sorted.

### 📂 [Bubble Sort](./array/bubble_sort)
- **Big O (Best):** O(n)
- **Big O (Average/Worst):** O(n²)
- **Description:** Repeatedly swaps adjacent elements if they’re in the wrong order. Very simple but inefficient.

### 📂 [Tree Sort](./array/tree_sort)
- **Big O (Best/Average):** O(n log n)
- **Big O (Worst):** O(n²)
- **Description:** Inserts elements into a binary search tree and then performs an in-order traversal.

### 📂 [Heap Sort](./array/heap_sort)
- **Big O (Best/Average/Worst):** O(n log n)
- **Description:** Builds a max heap and repeatedly extracts the largest element to sort the array in-place.

### 📂 [Quick Sort](./array/partition_sort)
- **Big O (Best/Average):** O(n log n)
- **Big O (Worst):** O(n²)
- **Description:** Uses divide-and-conquer with a pivot to partition and sort subarrays recursively.

---


[Media and License Attribution](/REFERENCES.md)
