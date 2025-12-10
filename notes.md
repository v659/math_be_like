Thanks to Chads Prep

2D VECTORS

vector = magnitude + direction

sin(theta) = opposite/hypot
cos(theta) = adjacent/hypot
tan(theta) = opposite/adjacent

Using sin and cos, we can derive the x and y components of a vector
If you calculated x and y components, you can use pythagorean's theorem to recalculate the hypot
Calculate angle is atan2(y, x)

Adding and subtracting - Just extract the x and y components, add or subtract them

1D kinematics

For 1D, we can just pad our 2D vector class like this:
position = Vector2Math(12, x=0, y=0)
velocity = Vector2Math(12, x=5, y=0)  # 5 m/s along x
acceleration = Vector2Math(12, x=2, y=0)  # 2 m/s² along x

Concept:
Displacement(m) is the vector from start point with the direction
Velocity(m/s) is vector of displacement/time in a direction displacement per time unit
Acceleration(m/s**2) is vector of velocity/time in a direction velocity change per time unit
Constant velocity = 0 acceleration

A = 0

Displacement = vt

a = constant
Law 1

Displacement = Avg.Velocity * t
Law 2

Avg velocity = (Final velocity + Init. Velocity)/2
displacement = (Final velocity + Init. Velocity)/2 * t
final velocity = v(i) + at
displacement = ((v(i) + (v(i) + at))/2) * t
= ((2v(i) + at) / 2) * t
= v(i)t + 1/2at**2
displacement = v(i)t + 1/2at**2
s = v(i)t + 1/2at**2
Law 3(not knowing the time)

- Substitute time for (v(f)-v(i))/a

- Substitute time from equation 2
First term
v(i)t = vi((vf - vi)/a)
= (vi(vf) - vi**2)/a
Second term
= 1/2at**2
= 1/2a((vf-vi)/a)**2
= 1/2a((vf-vi)**2/a**2))
= 1/2 * a/a**2 * (vf-vi)**2
a/a**2 = 1/a
1/2*1/a = 1/2a
((vf-vi)**2)/2a

Displacement = x
Together: displacement = (vi(vf) - vi**2)/a + ((vf-vi)**2)/2a
make a common denominator:
x = 2(vi(vf) - vi**2)/2a + ((vf-vi)**2)/2a
Make it a single fraction
x = (2(vi(vf) - vi**2) + ((vf-vi)**2))/2a
Distribute the 2 and use algebraic identity
x = ((2vi(vf) - 2(vi**2)) + (vf**2 - 2vf(vi) + vi**2))/2a
Cancel out common terms and combine
x = (vf**2 - vi**2)/2a

Rearrange
2ax = (vf**2 - vi**2)

vf**2 = vi**2 + 2ax





