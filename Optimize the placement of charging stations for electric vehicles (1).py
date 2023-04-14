#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math

# Define constants
NUM_CHARGING_STATIONS = 5
MAX_COORDINATE = 1000
MAX_CHARGING_RATE = 100
MAX_RANGE = 500
MAX_ITERATIONS = 100
POPULATION_SIZE = 100
C1 = 2.0
C2 = 2.0
W = 0.7

class Particle:
    def __init__(self):
        self.position = []
        self.velocity = []
        self.best_position = []
        self.fitness = float('inf')
        self.best_fitness = float('inf')

        # Initialize position and velocity
        for i in range(NUM_CHARGING_STATIONS):
            self.position.append(random.uniform(0, MAX_COORDINATE))
            self.velocity.append(random.uniform(-MAX_COORDINATE, MAX_COORDINATE))

    def evaluate_fitness(self):
        total_charging_time = 0
        total_range = 0

        # Calculate total charging time and range for each electric vehicle
        for ev in electric_vehicles:
            charging_times = []
            ranges = []

            for station in self.position:
                distance = abs(ev - station)
                charging_time = distance / MAX_CHARGING_RATE
                range = MAX_RANGE - distance
                if range < 0:
                    range = 0
                charging_times.append(charging_time)
                ranges.append(range)

            fastest_charging_time = min(charging_times)
            total_charging_time += fastest_charging_time
            max_range = max(ranges)
            total_range += max_range

        # Update fitness
        self.fitness = total_charging_time + (1 / total_range)

        # Update personal best
        if self.fitness < self.best_fitness:
            self.best_fitness = self.fitness
            self.best_position = self.position.copy()

class Swarm:
    def __init__(self):
        self.particles = []

        # Initialize particles
        for i in range(POPULATION_SIZE):
            self.particles.append(Particle())

    def run(self):
        global_best_fitness = float('inf')
        global_best_position = []

        for i in range(MAX_ITERATIONS):
            # Evaluate fitness for each particle
            for particle in self.particles:
                particle.evaluate_fitness()

                # Update personal and global best
                if particle.fitness < global_best_fitness:
                    global_best_fitness = particle.fitness
                    global_best_position = particle.position.copy()

            # Update position and velocity for each particle
            for particle in self.particles:
                for j in range(NUM_CHARGING_STATIONS):
                    r1 = random.uniform(0, 1)
                    r2 = random.uniform(0, 1)
                    particle.velocity[j] = (W * particle.velocity[j]) + (C1 * r1 * (particle.best_position[j] - particle.position[j])) + (C2 * r2 * (global_best_position[j] - particle.position[j]))
                    particle.position[j] = max(0, min(MAX_COORDINATE, particle.position[j] + particle.velocity[j]))

        return global_best_fitness, global_best_position

# Define electric vehicles
electric_vehicles = [100, 250, 400, 550, 700]

# Initialize swarm and run PSO
swarm = Swarm()
best_fitness, best_position = swarm.run()

# Print results
print("Best fitness: ", best_fitness)
print("Best position: ", best_position)


# In[ ]:




