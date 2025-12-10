from vector2D import Vector2Math
from kinematics import KinematicsBody, GRAVITY
import matplotlib.pyplot as plt
import matplotlib.animation as animation

angle = 30
init_velocity = 100

# Setup
velocity_vector = Vector2Math(12, angle=angle, hypot=init_velocity)
WIND_ACCELERATION = Vector2Math(12, x=-2, y=0)
position_vector = Vector2Math(12, x=0, y=0)
gravity_vector = GRAVITY
acceleration_vector = GRAVITY + WIND_ACCELERATION
body = KinematicsBody(position_vector, velocity_vector, acceleration_vector)

dt = 0.05
elapsed_time = 0
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 1200)
ax.set_ylim(0, 400)
ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Vertical Height (m)')
ax.set_title(f'Projectile Motion: {angle}° at {init_velocity} m/s')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linestyle='-', alpha=0.5)
trajectory_line, = ax.plot([], [], 'b-', alpha=0.7, linewidth=2)
projectile_point, = ax.plot([], [], 'ro', markersize=10, markeredgecolor='black')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
height_text = ax.text(0.02, 0.88, '', transform=ax.transAxes, fontsize=12,
                      bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

x_data, y_data = [], []


def init():
    trajectory_line.set_data([], [])
    projectile_point.set_data([], [])
    time_text.set_text('')
    height_text.set_text('')
    return trajectory_line, projectile_point, time_text, height_text


def animate(frame):
    global elapsed_time

    elapsed_time += dt
    body.update(dt)

    x_data.append(body.position.x)
    y_data.append(body.position.y)

    # Update plot
    trajectory_line.set_data(x_data, y_data)
    projectile_point.set_data([body.position.x], [body.position.y])

    time_text.set_text(f'Time: {elapsed_time:.1f} s')
    height_text.set_text(f'Height: {body.position.y:.1f} m')

    if body.position.y <= 0 < elapsed_time:
        ani.event_source.stop()
        ax.text(0.02, 0.81, f'LANDED!\nRange: {body.position.x:.1f} m',
                transform=ax.transAxes, fontsize=12,
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

    return trajectory_line, projectile_point, time_text, height_text


# Create animation
ani = animation.FuncAnimation(fig, animate, frames=500,
                              init_func=init, blit=True,
                              interval=50, repeat=False)

plt.tight_layout()
plt.show()
