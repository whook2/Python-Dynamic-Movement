# Will Hooker CS 330-01
import math
import classes
import move_functions


# Opening the text file in write mode
f = open("CS 330, Dynamic Trajectory Data.txt", "w")


# Function that prints all character data to the text file
def print_character(player, sim_time):
    f.write(str(sim_time) + ',' + str(player.id) + ',' + str(player.pos[0]) + ',' + str(player.pos[1]) + ',' +
            str(player.vel[0]) + ',' + str(player.vel[1]) + ',' + str(player.accel_x) + ',' + str(player.accel_z) +
            ',' + str(player.orient) + ',' + str(player.steering) + ',' + (str(player.collision).upper()))
    f.write('\n')


# Initialization of the characters
p1 = classes.Character(2601, [0, 0], [0, 0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, False, 0)  # Continue
p2 = classes.Character(2602, [-30, -50], [2, 7], 0, 0, (math.pi/4), 8, 1.5, 1, 0, 0, 0, 7, False, 0)  # Flee
p3 = classes.Character(2603, [-50, 40], [0, 8], 0, 0, ((3*math.pi)/2), 8, 2, 1, 0, 0, 0, 6, False, 0)  # Seek
p4 = classes.Character(2604, [50, 75], [-9, 4], 0, 0, math.pi, 10, 2, 1, 4, 32, 1, 8, False, 0)  # Arrive


# Initialization of time and timestep
time = 0
timestep = 0.5


# For loop that is used to increment the time and call the movement and update functions
for x in range(0, 101):

    # Calling the continue function for p1
    result = move_functions.cont(p1)
    p1.accel_x = result.linear[0]
    p1.accel_z = result.linear[1]
    p1.update(result, p1.max_velo, timestep)

    # Calling the flee function to update character 2's values
    result = move_functions.flee(p2, p1, p2.max_accel)
    p2.accel_x = result.linear[0]
    p2.accel_z = result.linear[1]
    p2.update(result, p2.max_velo, timestep)

    # Calling the seek function to update character 3's values
    result = move_functions.seek(p3, p1, p3.max_accel)
    p3.accel_x = result.linear[0]
    p3.accel_z = result.linear[1]
    p3.update(result, p3.max_velo, timestep)

    # Calling the arrive function to update character 4's values
    result = move_functions.arrive(p4, p1, p4.max_accel, p4.max_velo, p4.arrival_rad, p4.slow_rad, 0.1)
    p4.accel_x = result.linear[0]
    p4.accel_z = result.linear[1]
    p4.update(result, p4.max_velo, timestep)

    # Prints the initial character values first at time 0
    print_character(p1, time)  # Prints the continue character
    print_character(p2, time)  # Prints the flee character
    print_character(p3, time)  # Prints the seek character
    print_character(p4, time)  # Prints the arrive character

    # Increments the time by delta-t
    time += timestep


f.close()
