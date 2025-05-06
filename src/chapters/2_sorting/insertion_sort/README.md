# Insertion Sort

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Sorting_insertion_sort_anim.gif" alt="Insertion Sort Animation" width="400"/>
</p>

---

## 🧠 How It Works

Insertion sort builds a sorted array one item at a time by **repeatedly inserting elements into their correct position**. Think of how you might sort playing cards in your hands:

1. Start with an empty left hand and the cards face down on the table.
2. Pick up the cards one at a time from the table and insert them into the correct position in your hand.
3. Each insertion shifts elements as needed.

---

## 🧮 Algorithm Steps

Given an array of `n` elements:
1. Begin at the second element.
2. Compare it to the elements before it.
3. Shift larger elements one position to the right.
4. Insert the current element at the correct position.
5. Repeat until the array is sorted.

---

## ⏱️ Performance (Big O)

| Case        | Time Complexity | Description                         |
|-------------|------------------|-------------------------------------|
| Best Case   | O(n)             | Already sorted array.               |
| Average     | O(n²)            | Random order elements.              |
| Worst Case  | O(n²)            | Reversed order elements.            |
| Space       | O(1)             | In-place algorithm.                 |

---

## 📘 Book Reference

The illustration below is from the book and represents a conceptual view of array sorting:

<p align="center">
  <img src="/assets/insertion_sort.png" alt="Array Sorting Illustration" width="400"/>
</p>

