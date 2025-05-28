# Hilbert Curve

<p align="center">
  <img src="/assets/hilbert_curve3.png" alt="Recursion" width="400"/>
</p>
> output of of running included hilter_curve.py program

---

The Hilbert Curve is a fractal, that is curve which repeats itself; which is a perfect task for recursion. The hilbert curve has 3 shapes, all of which are comprised of the lower level. See image below:

<p align="center">
  <img src="/assets/hilbert_curve1.png" alt="Recursion" width="400"/>
</p>

The steps are a level-1 hilbert curve: 

> Let y = 90 degree
> 1) Rotate y degree towards the right
> 2) Move step size
> 3) Rotate y degree towards the left
> 4) Move step size
> 5) Rotate y degree towards the left
> 6) Move step size
> 7) Rotate y degree towards the right

And level-2:

> Rotate 90 degrees towards the right
> Create a hilbert curve at level 1 rotated by -y degrees (ie, y degrees in anticlockwise direction)
> Move step size
> Rotate y degrees towards the right
> Create a level 1 hilbert curve rotated by y degrees (ie, y degrees in clockwise direction)
> Rotate y degrees towards the left.
> Move step size
> Create a level 1 hilbert curve rotated by -y degrees
> Rotate y degrees towards the right

Manually drawing this on pen and paper following steps make internalizing this structure/algorithm a little easier. 

[Media and License Attribution](/REFERENCES.md)
