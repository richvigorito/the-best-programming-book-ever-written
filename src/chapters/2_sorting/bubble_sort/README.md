# Bubble Sort

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif" alt="Bubble Sort Animation" width="400"/>
</p>

---

## 🧠 How It Works

Bubble sort repeatedly steps through the list, compares adjacent elements, and **swaps them if they are in the wrong order**. This process continues until no more swaps are needed.

It’s called "bubble" sort because **smaller elements bubble to the top** (beginning of the array) with each pass. Read the except from the book below "the items as bubbles in a water tank ..."

---

## 🧮 Algorithm Steps

Given an array of `n` elements:
1. Compare the first two elements.
2. Swap if the first is greater than the second.
3. Move to the next pair and repeat.
4. After one full pass, the largest element will be at the end.
5. Repeat the pass, reducing the range by one each time, until sorted.

---

## ⏱️ Performance 

| Case        | Time Complexity | Description                         |
|-------------|------------------|-------------------------------------|
| Best Case   | O(n)             | Already sorted (optimized version). |
| Average     | O(n²)            | Typical case.                       |
| Worst Case  | O(n²)            | Reverse sorted array.               |
| Space       | O(1)             | In-place algorithm.                 |

---

## 📘 Book Reference

<p align="center">
  <img src="/assets/bubble_sort.png" alt="Bubble Sort Book Illustration" width="400"/>
</p>

> chapter 2, sec 2.2.3, page 65,66 

[Media and License Attribution](/REFERENCES.md)

