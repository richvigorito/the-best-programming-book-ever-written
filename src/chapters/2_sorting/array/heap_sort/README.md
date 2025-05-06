# Heap Sort

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif" alt="Heap Sort Animation" width="400"/>
</p>

---

## 🧠 How It Works

Heap sort uses a **binary heap** data structure to sort the elements. It first builds a max-heap and then repeatedly extracts the largest element and places it at the end of the array.

This maintains the sorted portion at the back and the unsorted portion as a valid heap.

---

## 🧮 Algorithm Steps

1. Build a max-heap from the input array.
2. Swap the first (largest) element with the last one.
3. Reduce the heap size and heapify the root.
4. Repeat until the heap is empty.

---

## ⏱️ Performance 

| Case        | Time Complexity | Description          |
|-------------|------------------|----------------------|
| Best Case   | O(n log n)       | Always guaranteed.   |
| Average     | O(n log n)       | Consistent behavior. |
| Worst Case  | O(n log n)       | No degradation.      |
| Space       | O(1)             | In-place.            |

---

## 📘 Book Reference

<p align="center">
  <img src="/assets/heap_sort.pg73.png" alt="Heap Sort Book Illustration" width="400"/>

  <img src="/assets/heap_sort.pg74.png" alt="Heap Sort Book Illustration" width="400"/>
</p>

> chapter 2, sec 2.2.5, page 73,74

<sub>[Media and License Attribution](/REFERENCES.md)</sub>
