import classes
import helper_functions


# The Continue movement function
def cont(character):
    # Create output structure
    result = classes.SteeringOutput([0, 0], 0)

    # Assigning the pre-existing linear acceleration
    result.linear[0] = character.accel_x
    result.linear[1] = character.accel_z
    result.angular = 0

    # Output steering
    return result


# The Seek movement function
def seek(character, target, max_accel):
    # Create output structure
    result = classes.SteeringOutput([0, 0], 0)

    # Get the direction to the target
    result.linear[0] = target.pos[0] - character.pos[0]
    result.linear[1] = target.pos[1] - character.pos[1]

    # Accelerate at maximum rate
    result.linear = helper_functions.normalize(result.linear)
    result.linear[0] *= max_accel
    result.linear[1] *= max_accel

    # Output steering
    result.angular = 0
    return result


# The Flee movement function
def flee(character, target, max_accel):
    # Create output structure
    result = classes.SteeringOutput([0, 0], 0)

    # Get the direction to the target
    result.linear[0] = character.pos[0] - target.pos[0]
    result.linear[1] = character.pos[1] - target.pos[1]

    # Accelerate at maximum rate
    result.linear = helper_functions.normalize(result.linear)
    result.linear[0] *= max_accel
    result.linear[1] *= max_accel

    # Output steering
    result.angular = 0
    return result


# The Arrive movement function
def arrive(character, target, max_accel, max_speed, target_radius, slow_radius, time_to_target):
    # Create output structure
    result = classes.SteeringOutput([0, 0], 0)

    # Get the direction and distance to the target
    direction = [0, 0]
    direction[0] = target.pos[0] - character.pos[0]
    direction[1] = target.pos[1] - character.pos[1]
    distance = helper_functions.length(direction)

    # Test for arrival
    if distance < target_radius:
        return classes.SteeringOutput([0, 0], 0)

    # Outside slowing-down (outer) radius, move at max speed
    if distance > slow_radius:
        target_speed = max_speed

    # Between radii, scale speed to slow down
    else:
        target_speed = max_speed * (distance / slow_radius)

    # Target velocity combines speed and direction
    target_velocity = direction
    target_velocity = helper_functions.normalize(target_velocity)
    target_velocity[0] *= target_speed
    target_velocity[1] *= target_speed

    # Accelerate to target velocity
    result.linear[0] = target_velocity[0] - character.vel[0]
    result.linear[1] = target_velocity[1] - character.vel[1]
    result.linear[0] /= time_to_target
    result.linear[1] /= time_to_target

    # Test for too fast acceleration
    if helper_functions.length(result.linear) > max_accel:
        result.linear = helper_functions.normalize(result.linear)
        result.linear[0] *= max_accel
        result.linear[1] *= max_accel

    # Output steering
    result.angular = 0
    return result
