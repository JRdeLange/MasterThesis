import math

graphics = True

speedup = 1

# World
# The number of observed agents does not include itself or the predator
nr_observed_agents = 3
nr_of_boids = 19
predator_present = True
grouped_spawn = True
predator_halting = True

# Boid
boid_speed = 0.01
boid_color = (0.8, 0.8, 0.8, 1)
boid_turning_speed = 0.02 * math.pi / speedup

# Predator
predator_speed = 0.011
predator_lunging = True
predator_lunge_speed = 0.013
predator_lunge_distance = 0.3 * speedup
predator_turning_speed = 0.016 * math.pi / speedup
predator_color = (0.8, 0.2, 0.2, 1)
predator_confusion = True
predator_confusion_distance = .4
predator_confusion_threshold = 3
predator_chase_time = 30
predator_halt_time = 45
predator_eating_distance = 0.06 * speedup

# Window
height = 800
width = 800
