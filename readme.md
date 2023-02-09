## Do agents learn to flock under predatory pressure?

A series of 2D and 3D models where boid-like agents try to survive a predator hunting them down. The objective of the thesis this code is written for is to determine whether predatory pressure can induce flocking behaviour in 2D as well as in 3D.

All models are built to work with the DQN agent provided [here](https://github.com/keras-rl/keras-rl). 

The structure of all models is as follows. *config.py* contains all customizable parameters. *main.py* populates the world with the boids and the predator, initializes the DQN agent and readies the environment for the agent. The agent is then set to train or run for a set amount of steps. Each step the agent calls *step* in *environment.py* and passes it its action. This is then executed, the model is progressed a step and information is passed back to the agent on which it bases its next action. In the case the agent is training, only one boid (*the_one*) actually trains, all the other boid simply utilize the only training boids network to determine their actions.

Finished models are in the root, models that are still being worked on are in *Unfinished models*, models that are only kept around because I still might need code from them are in *Unfinished models/Scrapped models*
