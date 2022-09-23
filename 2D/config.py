#todo verify rotation info correct for boids and predator
#todo verify direction element of observation


import math

graphics = True

speedup = .33

# World
# The number of observed agents does not include itself or the predator
nr_observed_agents = 5
nr_of_boids = 10
predator_present = True
grouped_spawn = True
predator_halting = True

# Boid
boid_speed = 0.0333 #from OG, 1/60th of space per step
boid_color = (0.8, 0.8, 0.8, 1)
boid_turning_speed = 0.5 * math.pi

# Predator
predator_speed = 0.0333 #from OG, 1/60th of space per step
predator_speed_slow = 0.0333
predator_speed_fast = 0.0533
predator_lunging = True
predator_lunge_speed = 0.013
predator_lunge_distance = 0.3 * speedup
predator_turning_speed = .25 * math.pi
predator_color = (0.8, 0.2, 0.2, 1)
predator_confusion = True
predator_confusion_distance = .4 #from OG, .2 of space
predator_confusion_threshold = 2
predator_chase_time = 20
predator_halt_time = 0
predator_eating_distance = 0.06666 #from OG, eat if distance is less than 2/60th of space

# Window
height = 800
width = 800
