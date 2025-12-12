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

Kinematics

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

Law 4

v(f) = vi + at
Very simple - Pure intuition

Dynamics

Newtons laws:
1. F=ma
2. If Net Force = 0, v = constant
3. For every action (force) in nature there is an equal and opposite reaction

Gravity

F = (G(constant) * (m1*m2))/r**2
r = Distance between 2 centers of mass for the body

Drag:

This one took some time to understand:

So the equation is:
F_drag = 0.5 * rho * C_d * A * v**2

Now how did we get this???

So basically, let us first see the components:
We have rho(the air density)
We have v(the velocity of our object)
We have A(Frontal area of the object)
We have C_d(Drag coefficient, basically how much the objects shape disturbs the air)

So for one part of the equation, we have a special equation related to fluid pressure, because air is a fluid:

q = 1/2(pv**2)
q is dynamic pressure, so kinetic energy per volume -
q = KE/V
KE(Kinetic energy is from the work equation)
V(Volume)
So lets solve for KE:
Work = f * d
Work = ma * d

Lets look at our kinematics equations again and get one without time to find displacement:

v(f) = v(i) ** 2 + 2ax

We assume init. vel is 0
v(f) ** 2 = 2ax
x = v ** 2/2a
So, we put the 2 parts together:

Work = m * a * v ** 2/2a
Work = m * av ** 2/2a
Work = m * 1/2 * v ** 2
Over here, our mass becomes pV, where:
p = pressure and v = volume, so we have:
Work = pV * 1/2 * v ** 2.
Now, we have:
q = pV * 1/2 * v ** 2 / V
q = p * 1/2 * v ** 2
q = 1/2 * p * v**2

With this done, we have to see about the drag coefficient and Area:

They are both directly proportional to the Drag force, so we have:
F_drag = q * C_d * A
Plug the q in:
F_drag = 1/2 * p * v**2 * C_d * A

Now we just rename the p to rho because its density, while p is preserved for pressure

F_drag = 1/2 * rho * v**2 * C_d * A

We still need to derive a couple more equations to have a COMPLETE set.

rho equation is pretty simple:
m/V
Mass/volume of the fluid

C_d is determined through experimentation, but if you have F_drag:
C_d = F_d / (0.5 * rho * v**2 * A)


