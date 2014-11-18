import utils
import numpy

class Model(object):
    def __init__(self):
        self._start, self._end = numpy.array([0.0, 0.0]), numpy.array([0.0, -200.0])
        self.v = self._end - self._start
        self.v /= numpy.linalg.norm(self.v)
        self._normal = numpy.array([self.v[1], -self.v[0]])
        
    def set_state(self, state):
        self.tf = utils.rotate(state[0])

    def evaluate(self, t):
        return (self.end - self.start) * t + self.start
#        pt = (self.end - self.start) * t + self.start
#        return numpy.dot(self.tf, pt)

    def normal(self, t):
        return numpy.dot(self.tf, self._normal)
        

    def get_start(self):
        return numpy.dot(self.tf, self._start)
    start = property(get_start)

    def get_end(self):
        return numpy.dot(self.tf, self._end)
    end = property(get_end)

    def get_ball(self):
        return self.end + numpy.dot(self.tf, 15.0 * self.v)
    ball = property(get_ball)
