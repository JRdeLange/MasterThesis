import math


class Config:

    def __init__(self, configuration=0):
        # "Standard" configuration:
        self.run_name = "test"

        # Training:
        self.linear_annealing = True
        self.linear_annealing_from = 0.1
        self.linear_annealing_to = 0.001

        # World
        # The number of observed agents does not include itself or the predator
        self.nr_observed_agents = 5
        self.nr_of_boids = 8      # on top of The One
        self.predator_present = True
        self.grouped_spawn = False
        self.predator_halting = False

        # Collect data for analysis
        self.record_keeping = True
        # Gather data every gather_frequency ticks
        self.record_frequency = 1000

        # Boid
        self.boid_speed = 0.0333  # from OG, 1/60th of space per step
        self.boid_color = (0.8, 0.8, 0.8, 1)
        self.boid_turning_speed = 0.5 * math.pi  # From OG, 90 degrees

        # Predator
        self.predator_speed = 0.0333  # from OG, 1/60th of space per step
        self.predator_speed_slow = 0.0333
        self.predator_speed_fast = 0.0533
        self.predator_lunging = False
        self.predator_lunge_speed = 0.013
        self.predator_lunge_distance = 0.1
        self.predator_turning_speed = .25 * math.pi
        self.predator_color = (0.8, 0.2, 0.2, 1)
        self.predator_confusion = True
        self.predator_confusion_distance = .4  # from OG, .2 of space
        self.predator_confusion_threshold = 2
        self.predator_chase_time = 20
        self.predator_halt_time = 0
        self.predator_eating_distance = 0.06666  # from OG, eat if distance is less than 2/60th of space

        # Window
        self.height = 800
        self.width = 800
        self.graphics = True

        self.change_to_configuration(configuration)

    def change_to_configuration(self, configuration):
        if configuration == 1:
            self.run_name = "12_other_boids"
            self.nr_of_boids = 12
