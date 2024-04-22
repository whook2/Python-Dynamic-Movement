import helper_functions


# Declaration of the SteeringOutput class
class SteeringOutput:
    def __init__(self, linear, angular):
        self.linear = linear
        self.angular = angular


# Declaration of the Character class
class Character:
    def __init__(self, ident, pos, vel, accel_x, accel_z, orient, max_velo, max_accel, target,
                 arrival_rad, slow_rad, time_to_target, steering, collision, rotation):
        self.id = ident
        self.pos = pos
        self.vel = vel
        self.accel_x = accel_x
        self.accel_z = accel_z
        self.orient = orient
        self.max_velo = max_velo
        self.max_accel = max_accel
        self.target = target
        self.arrival_rad = arrival_rad
        self.slow_rad = slow_rad
        self.time_to_target = time_to_target
        self.steering = steering
        self.collision = collision
        self.rotation = rotation

# Character update function
    def update(self, steering, max_speed, time):
        # Update the position and orientation
        self.pos[0] += self.vel[0] * time
        self.pos[1] += self.vel[1] * time
        self.orient += self.rotation * time

        # Update the velocity and rotation
        self.vel[0] += steering.linear[0] * time
        self.vel[1] += steering.linear[1] * time
        self.rotation += steering.angular * time

        # Check for speed above max and clip
        if helper_functions.length(self.vel) > max_speed:
            self.vel = helper_functions.normalize(self.vel)
            self.vel[0] *= max_speed
            self.vel[1] *= max_speed
