import settings
import numpy

class Dynamics(object):
    def __init__(self):
        self.num_particles = settings.num_particles
#        self.particles = numpy.array([0.0] * self.num_particles)
        self.particles = settings.initialization_func()

    def step(self):
        for i in range(self.num_particles):
            self.particles[i] += settings.noise_func()
