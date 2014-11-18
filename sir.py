import math
import numpy
import time
import settings

def timer(func):
    before = time.time()
    func()
    after = time.time()
    return after - before

class Sir():
    """
    http://en.wikipedia.org/wiki/Particle_filter
    Sequential importance resampling
    """
    def __init__(self, num_particles, N_thr, state_dim, obs_model, dyn_model):
        self.num_particles, self.N_thr, self.state_dim, self.obs_model, self.dyn_model = num_particles, N_thr, state_dim, obs_model, dyn_model

        self.counter = 0
        self.N_eff = 0.0
        self.mean = numpy.zeros(state_dim)
        self.weights = numpy.ones(self.num_particles)
        self.likelihood = numpy.ones(self.num_particles)
        self.timing = [0.0] * 6
        # Pointers in Python. Share the particles array between the objects.
        self.particles = self.dyn_model.particles 
        self.obs_model.particles = self.particles
        self.tree = []

    def compute_prior(self):
        before = self.particles.copy()
        self.dyn_model.step()
        after = self.particles.copy()
        self.tree.append((before, after))

    def compute_observation(self):
        self.likelihood[:] = self.obs_model.compute()

    def multiply_weights(self):
        for i in range(len(self.weights)):
            self.weights[i] *= self.likelihood[i]

    def normalize(self):
        sum_ = numpy.sum(self.weights)
        self.weights /= sum_
        
    def compute_num_effective_particles(self):
        self.N_eff = 1.0 /  numpy.sum(numpy.dot(self.weights, self.weights))
        
    def calc_mean(self):
        self.mean[:] = numpy.dot(self.weights, self.particles)

    def reorder_particles(self, indices):
        particles = numpy.empty_like(self.particles)
        for i, idx in enumerate(indices):
            particles[i] = self.particles[indices[idx]]
        return particles

    def systematic_resampling(self):
        # A Tutorial on Particle Filtering and Smoothing:
        # Fifteen years later
        # Arnaud Doucet and Adam M. Johansen
        # 2008
        # Section 3.4
        N, w = self.num_particles, self.weights

        indices = range(N)

        w_cumsum = numpy.cumsum(self.weights).tolist()
        w_cumsum.insert(0, 0.0)

        # Sample U_1 \approx uniform distribution [0, 1/N]
        rnd = numpy.random.rand(1)[0] / N
        delta = 1.0 / N

        N_list = [0] * N

        for i in range(N):
            w_lower = w_cumsum[i]
            w_upper = w_cumsum[i+1]
            lower = math.ceil((w_lower - rnd) / delta)
            upper = math.ceil((w_upper - rnd) / delta)
            if upper > lower:
                N_list[i] = int(upper - lower)

        _indices_new = []

        for i in range(len(N_list)):
            if N_list[i] > 0:
                _indices_new.extend([indices[i]] * N_list[i])

        self.weights[:] = numpy.array([1.0 / N] * N)
        self.particles[:] = self.reorder_particles(_indices_new)

    def step(self):
        self.counter += 1
        timing = []
        timing.append(timer(self.compute_prior))        
        timing.append(timer(self.compute_observation))
        timing.append(timer(self.multiply_weights))
        timing.append(timer(self.normalize))
        timing.append(timer(self.compute_num_effective_particles))
        timing.append(timer(self.systematic_resampling))

        for i, t in enumerate(timing):
            self.timing[i] += t

        self.calc_mean()



