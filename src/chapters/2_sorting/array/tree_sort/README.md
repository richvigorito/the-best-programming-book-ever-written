# Tree Sort

## 🧠 How It Works

Tree sort builds a **binary search tree (BST)** from the elements of the input array, then performs an **in-order traversal** to retrieve them in sorted order.

Each insertion ensures that the tree maintains its order: left children are smaller, right children are greater.

---

## 🧮 Algorithm Steps

1. Create an empty binary search tree.
2. Insert all elements from the input array into the BST.
3. Traverse the BST in-order to collect the sorted elements.

---

## ⏱️ Performance 

| Case        | Time Complexity | Description                            |
|-------------|------------------|----------------------------------------|
| Best Case   | O(n log n)       | Balanced tree.                         |
| Average     | O(n log n)       | Random insertions.                     |
| Worst Case  | O(n²)            | Degenerate tree (e.g. sorted input).   |
| Space       | O(n)             | New tree created.                      |

---

## 📘 Book Reference

<p align="center">
  <img src="/assets/tree_sort.png" alt="Tree Sort Book Illustration" width="400"/>
</p>

> chapter 2, sec 2.2.X, page XX

<sub>[Media and License Attribution](/REFERENCES.md)</sub>
