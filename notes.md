# Thanks to Chads Prep

## 2D VECTORS

A **vector** = magnitude + direction.

### Basic Trig

-   **sin(θ)** = opposite / hypotenuse
-   **cos(θ)** = adjacent / hypotenuse
-   **tan(θ)** = opposite / adjacent

Using **sin** and **cos**, we can derive the **x** and **y** components
of a vector.\
If you have x and y components, you can use the **Pythagorean theorem**
to recalculate the hypotenuse.

To calculate the angle:

    angle = atan2(y, x)

### Adding and subtracting vectors

Extract the **x** and **y** components and add/subtract them separately.

------------------------------------------------------------------------

## 1D Kinematics

For 1D motion, we can "pad" our 2D vector class like this (keep y = 0):

``` python
position = Vector2Math(12, x=0, y=0)
velocity = Vector2Math(12, x=5, y=0)        # 5 m/s along x
acceleration = Vector2Math(12, x=2, y=0)    # 2 m/s² along x
```

### Concepts

-   **Displacement (m)**: the vector from start point in a direction\
-   **Velocity (m/s)**: displacement per unit time in a direction\
-   **Acceleration (m/s²)**: velocity change per unit time in a
    direction\
-   **Constant velocity** → acceleration = 0

### If acceleration A = 0

    Displacement = v * t

------------------------------------------------------------------------

## Constant Acceleration

Start with:

    Displacement = Avg. Velocity * t
    Avg. Velocity = (Final velocity + Initial velocity) / 2

So:

    displacement = (Final velocity + Initial velocity)/2 * t

Use:

    final velocity = v(i) + a t

Substitute:

    displacement = ((v(i) + (v(i) + a t)) / 2) * t
                 = ((2v(i) + a t) / 2) * t
                 = v(i)t + 1/2 a t²

Final formula:

    displacement = v(i)t + 1/2 a t²
    s = v(i)t + 1/2 a t²
