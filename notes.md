# Physics Notes: 2D Vectors & 1D Kinematics
*Thanks to Chad's Prep*

## 2D VECTORS

### Vector Basics
**vector = magnitude + direction**

### Trigonometry for Vectors
**sin(θ) = opposite/hypotenuse**  
**cos(θ) = adjacent/hypotenuse**  
**tan(θ) = opposite/adjacent**

### Vector Components
- Using sin and cos, we can derive the **x and y components** of a vector
- If you calculated x and y components, you can use **Pythagorean theorem** to recalculate the hypotenuse
- Calculate angle: **atan2(y, x)**

### Vector Operations
- **Adding and subtracting**: Just extract the x and y components, add or subtract them

---

## 1D KINEMATICS

### Representing 1D Motion with 2D Vectors
For 1D motion, we can use our 2D vector class like this:
position = Vector2Math(12, x=0, y=0)
velocity = Vector2Math(12, x=5, y=0) # 5 m/s along x
acceleration = Vector2Math(12, x=2, y=0) # 2 m/s² along x


### Key Concepts
- **Displacement (m)**: Vector from start point with direction
- **Velocity (m/s)**: Vector of displacement/time in a direction (displacement per time unit)
- **Acceleration (m/s²)**: Vector of velocity/time in a direction (velocity change per time unit)
- **Constant velocity = 0 acceleration**

### Special Case: Zero Acceleration (a = 0)
**Displacement = v × t**

### General Case: Constant Acceleration (a = constant)

#### **Law 1: Displacement from Average Velocity**
**Displacement = Avg.Velocity × t**

#### **Law 2: Deriving Displacement Formula**
Avg velocity = (Final velocity + Initial Velocity)/2
displacement = (Final velocity + Initial Velocity)/2 × t

final velocity = v(i) + at
displacement = ((v(i) + (v(i) + at))/2) × t
= ((2v(i) + at) / 2) × t
= v(i)t + 1/2at²

displacement = v(i)t + 1/2at²
s = v(i)t + 1/2at²


#### **Law 3: Velocity-Squared Relation (No Time Information)**

**Step 1: Substitute time from v = u + at**
**t = (v(f) - v(i))/a**

**Step 2: Substitute into displacement formula**  
**First term:**
v(i)t = vi((vf - vi)/a)
= (vi(vf) - vi²)/a

**Second term:**
1/2at² = 1/2a((vf-vi)/a)²
= 1/2a((vf-vi)²/a²)
= 1/2 × a/a² × (vf-vi)²
a/a² = 1/a
1/2×1/a = 1/2a
((vf-vi)²)/2a

**Step 3: Combine terms**
Displacement = x
x = (vi(vf) - vi²)/a + ((vf-vi)²)/2a

**Step 4: Common denominator**
x = 2(vi(vf) - vi²)/2a + ((vf-vi)²)/2a

**Step 5: Single fraction**
x = (2(vi(vf) - vi²) + ((vf-vi)²))/2a

**Step 6: Expand and simplify**
x = ((2vi(vf) - 2(vi²)) + (vf² - 2vf(vi) + vi²))/2a
Cancel out common terms and combine:
x = (vf² - vi²)/2a

**Step 7: Final rearrangement**
2ax = (vf² - vi²)
vf² = vi² + 2ax


---

## Summary of 1D Kinematic Equations

| Law | Equation | Use When... |
|-----|----------|-------------|
| 1 | v = u + at | You need velocity, know acceleration and time |
| 2 | s = ut + ½at² | You need displacement, know velocity, acceleration and time |
| 3 | v² = u² + 2as | You need velocity or displacement, **don't know time** |
