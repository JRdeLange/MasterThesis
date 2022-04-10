import math

graphics = True

# Environment
# The number of observed agents includes the predator
nr_observed_agents = 4
nr_of_boids = 8

# Boid
boid_speed = 0.01
boid_color = (0.8, 0.8, 0.8, 1)

# Predator
predator_speed = 0.012
predator_lunging = True
predator_lunge_speed = 0.02
predator_lunge_distance = 0.3
predator_turning_speed = .03 * math.pi
predator_color = (0.8, 0.2, 0.2, 1)
predator_confusion = True
predator_confusion_distance = .2
predator_confusion_threshold = 5
predator_chase_time = 3 * 60
predator_eating_distance = 0.02

# Window
height = 800
width = 800


