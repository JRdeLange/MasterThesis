import math


class Config:

    def __init__(self, configuration=0):
        # "Standard" configuration:
        self.run_name = "2D_rec_20_total_boids"

        self.annealing = True
        self.annealing_start = 0.2
        self.annealing_end = 0.002

        # World
        # The number of observed agents does not include itself or the predator
        self.nr_observed_agents = 5
        self.nr_of_boids = 19      # on top of The One
        self.predator_present = True
        self.grouped_spawn = False
        self.predator_halting = False

        # Collect data for analysis
        self.record_keeping = True
        # Gather data every gather_frequency ticks
        # for exp gather every 100
        # for training gather every 1000
        self.record_frequency = None
        self.exp_folder_name = "big network 5 observed"

        # Boid
        # faster is 0.0383
        # OG is 0.0333
        # slower is 0.0283
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
        self.predator_halt_time = 20
        self.predator_eating_distance = 0.06666  # from OG, eat if distance is less than 2/60th of space

        # Window
        self.height = 800
        self.width = 800
        self.graphics = True

        self.change_to_configuration(configuration)

    def change_to_configuration(self, configuration):
        if configuration == 1:
            self.run_name = "2D_rec_10_total_boids"
            self.boid_speed = 0.0333
            self.nr_of_boids = 9
            self.predator_chase_time = 20
        if configuration == 2:
            self.run_name = "2D_rec_10_total_boids_short_chase"
            self.boid_speed = 0.0333
            self.nr_of_boids = 9
            self.predator_chase_time = 10
        if configuration == 3:
            self.run_name = "2D_rec_10_total_boids_slower"
            self.boid_speed = 0.0283
            self.nr_of_boids = 9
            self.predator_chase_time = 20
        if configuration == 4:
            self.run_name = "2D_rec_10_total_boids_slower_short_chase"
            self.boid_speed = 0.0283
            self.nr_of_boids = 9
            self.predator_chase_time = 10
        if configuration == 5:
            self.run_name = "2D_rec_20_total_boids"
            self.boid_speed = 0.0333
            self.nr_of_boids = 19
            self.predator_chase_time = 20
        if configuration == 6:
            self.run_name = "2D_rec_20_total_boids_short_chase"
            self.boid_speed = 0.0333
            self.nr_of_boids = 19
            self.predator_chase_time = 10
        if configuration == 7:
            self.run_name = "2D_rec_20_total_boids_slower"
            self.boid_speed = 0.0283
            self.nr_of_boids = 19
            self.predator_chase_time = 20
        if configuration == 8:
            self.run_name = "2D_rec_20_total_boids_slower_short_chase"
            self.boid_speed = 0.0283
            self.nr_of_boids = 19
            self.predator_chase_time = 10
        '''
        if configuration == 1:
            self.run_name = "2D_rec_control_15_total_boids"
            self.nr_of_boids = 14
        if configuration == 2:
            self.run_name = "2D_rec_control_20_total_boids"
            self.nr_of_boids = 19
        if configuration == 3:
            self.run_name = "2D_rec_10_total_boids"
            self.nr_of_boids = 9
            self.nr_observed_agents = 0
            self.predator_present = True
        if configuration == 4:
            self.run_name = "2D_rec_10_total_boids_slower"
            self.nr_of_boids = 9
            self.boid_speed = 0.0283
            self.predator_present = True
        '''