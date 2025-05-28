# 🌀 Hilbert Curve

<p align="center">
  <img src="/assets/hilbert_curve3.png" alt="Recursion" width="400"/>
</p>

> 🎯 Output of the included `hilbert_curve.py` program

---

## 🔁 What Is a Hilbert Curve?

The **Hilbert Curve** is a fractal — a geometric shape that repeats itself at smaller scales — making it an ideal task for recursion. It consists of three base shapes, each constructed from a version of itself.

<p align="center">
  <img src="/assets/hilbert_curve1.png" alt="Hilbert Curve Breakdown" width="400"/>
</p>

> 📖 From Chapter 3, Section 3.3 — Pages 130–131

---

## 📐 Recursive Steps

### Level 1 Hilbert Curve

> Let **y = 90°**:
> 
> 1️⃣ Rotate y degrees **right**  
> 2️⃣ Move forward one step  
> 3️⃣ Rotate y degrees **left**  
> 4️⃣ Move forward one step  
> 5️⃣ Rotate y degrees **left**  
> 6️⃣ Move forward one step  
> 7️⃣ Rotate y degrees **right**

---

### Level 2 Hilbert Curve

> 1️⃣ Rotate 90° **right**  
> 2️⃣ Draw level-1 Hilbert Curve rotated **-y** (left)  
> 3️⃣ Move forward  
> 4️⃣ Rotate 90° **right**  
> 5️⃣ Draw level-1 Hilbert Curve rotated **+y** (right)  
> 6️⃣ Rotate 90° **left**  
> 7️⃣ Move forward  
> 8️⃣ Draw level-1 Hilbert Curve rotated **-y**  
> 9️⃣ Rotate 90° **right**

---

## ✍️ Pro Tip

Manually drawing this on paper while following the recursive rules can help internalize how the structure unfolds. Recursion becomes a lot more intuitive when you can *see* it step-by-step.

---

## 🛠️ How to Run

Run the Python file and follow the prompts:

```bash
python3 hilbert_curve.py
```

You'll be able to:
- Set recursion **depth**
- Control **drawing speed**
- Add a **pause** between steps
- Watch each recursive level draw in a **different color**
- See printed logs showing how recursion flows 🔍

---

## 📚 References

[Media and License Attribution](/REFERENCES.md)
Media and License Attribution](/REFERENCES.md)
