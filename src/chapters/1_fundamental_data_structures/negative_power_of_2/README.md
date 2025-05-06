## 🧮 How This Pascal Program Computes Negative Powers of 2

This elegant Pascal program simulates computing the decimal representation of negative powers of 2 — like:

- `2^(-1) = 0.5`
- `2^(-2) = 0.25`
- `2^(-3) = 0.125`
- …

### ❓ What's the Goal?

The idea is to **manually compute** these decimal values without using floating-point math.

It does this by:
- Representing the number as an array of decimal digits
- Simulating **long division by 2** on those digits

---

### 🔢 The Core Strategy

1. Start with the number `1.0000...` (as an array of digits)
2. Repeatedly divide the number by `2`, using digit-by-digit long division
3. After each division, the array contains the decimal digits of `2^-k`

---

### 💡 How the Algorithm Works

```pascal
const n = 10;
type digit = 0..9;
var i, k, r: integer;
    d: array[1..n] of digit;

begin
  d[1] := 1;
  for i := 2 to n do d[i] := 0;

  for k := 1 to n do
  begin
    write(',');
    r := 0;
    for i := 1 to n do
    begin
      r := 10 * r + d[i];
      d[i] := r div 2;
      r := r mod 2;
      write(chr(d[i] + ord('0')));
    end;
  end;
end.
```

---

### 🔍 Step-by-Step Breakdown

- The `d` array holds the digits of the decimal value (like `[1, 0, 0, 0, ...]`)
- Each iteration of `k` divides the current number by 2
- The `for i := 1 to n` loop performs long division:
  - Multiply the remainder `r` by 10 and add the digit
  - Divide by 2 → this is the new digit
  - Remainder carries to the next digit

Example:
```
Start: 1.0000000000
1st ÷2: 0.5000000000
2nd ÷2: 0.2500000000
3rd ÷2: 0.1250000000
```

---

### 🤔 Why Not Just Use Floats?

- In the 1970s, floating-point math was **not portable or reliable**
- This approach:
  - Works the same on every machine
  - Is **precise** (no rounding surprises)
  - Shows how to build numeric computation from scratch

---

### 🧠 Key Learning

This program is a hands-on example of:
- Simulating real-number arithmetic using integers
- Handling decimal representation manually
- Understanding division at a deep, bitwise level

---
### 📷 Snapshot from the Book
This program is featured in the original text and shows how to compute negative powers of 2 using only integer arithmetic.

<p align="center">
  <img src="/assets/neg_pow_2.png" alt="Negative Power of 2 Pascal Program">
</p>
> chapter 1, sec 1.6, page 15
