# Quick Sort

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif" alt="Quick Sort Animation" width="400"/>
</p>

---

## 🧠 How It Works

Quick sort selects a **pivot**, partitions the array so elements less than the pivot go left, greater go right, and recursively sorts both halves.

Its power lies in the partitioning step and **divide-and-conquer** strategy.

---

## 🧮 Algorithm Steps

1. Choose a pivot element.
2. Partition the array around the pivot.
3. Recursively apply the process to the subarrays.

---

## ⏱️ Performance 

| Case        | Time Complexity | Description                     |
|-------------|------------------|---------------------------------|
| Best Case   | O(n log n)       | Balanced partitions.            |
| Average     | O(n log n)       | Random pivots.                  |
| Worst Case  | O(n²)            | Poor pivot (e.g. sorted input). |
| Space       | O(log n)         | Due to recursion stack.         |

---

## 📘 Book Reference

<p align="center">
  <img src="/assets/quick_sort.png" alt="Quick Sort Book Illustration" width="400"/>
</p>

> chapter 2, sec 2.2.6, page 76,77

<sub>[Media and License Attribution](/REFERENCES.md)</sub>
