import utils
import numpy

class Line(object):
    def __init__(self, start, end):
        self._start, self._end = numpy.array(start).astype(numpy.float), numpy.array(end).astype(numpy.float)

        self.v = self._end - self._start
        self.v /= numpy.linalg.norm(self.v)
        self._normal = numpy.array([self.v[1], -self.v[0]])

    def set_tf(self, tf):
        self.tf = tf

    def get_start(self):
        return numpy.dot(self.tf, self._start)
    start = property(get_start)

    def get_end(self):
        return numpy.dot(self.tf, self._end)
    end = property(get_end)

    def get_normal(self):
        return numpy.dot(self.tf, self._normal)
    normal = property(get_normal)

    def get_direction(self):
        return numpy.dot(self.tf, self.v)
    direction = property(get_direction)
    

class Model(object):
    def __init__(self):
        self.lines = [Line([0, -10], [0, -200]), Line([0, 10], [0, 200])]

        self._start, self._end = numpy.array([0.0, 0.0]), numpy.array([0.0, -200.0])
        self.v = self._end - self._start
        self.v /= numpy.linalg.norm(self.v)
        self._normal = numpy.array([self.v[1], -self.v[0]])
        
    def set_state(self, state):
        self.tf = utils.rotate(state[0])
        for line in self.lines:
            line.set_tf(self.tf)

    def _get_idx(self, t):
        idx = int(t * len(self.lines))
        if idx >= len(self.lines):
            idx = len(self.lines)-1
        return idx

    def evaluate(self, t):
        idx = self._get_idx(t)

        N = len(self.lines)        
        tt = (t - 1.0/float(N)*idx) / 0.5
        return (self.lines[idx].end - self.lines[idx].start) * tt + self.lines[idx].start

    def normal(self, t):
        return self.lines[self._get_idx(t)].normal

    # def get_start(self):
    #     return numpy.dot(self.tf, self._start)
    # start = property(get_start)

    # def get_end(self):
    #     return numpy.dot(self.tf, self._end)
    # end = property(get_end)

    def get_ball(self):
        return self.lines[0].end + 15.0 * self.lines[0].direction
    ball = property(get_ball)
