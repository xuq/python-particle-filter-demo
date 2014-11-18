import settings
import cPickle as pickle
import Image
import numpy
import model
import os
import utils

origo = numpy.array(settings.origo)

utils.mkdir(settings.tmp_dir)

class ObservationModel(object):
    def __init__(self):
        self.data = pickle.load(open(settings.source_data))
        self.counter = 0
        self.num_particles = settings.num_particles

    def set_particles(self, particles):
        self.particles = particles

    def load_image(self):
        image_path = os.path.join(settings.source_image_dir, 'image%06d.png' % self.counter)
        return numpy.array(Image.open(image_path))

    def px(self, pt):
        u,v = int(pt[0]), -int(pt[1])
        if v < 0 or v >= self.img.shape[0]:
            return 0.0
        if u < 0 or u >= self.img.shape[1]:
            return 0.0
        self.debug_img[v,u] = 0
        return 255.0 - self.img[v, u]

    def detect_edge(self, pt, normal):
        p, n = pt, 8 * normal
        px1, px2, px3 = self.px(p), self.px(p+n), self.px(p-n)
        return (px1 - px2)**2 + (px1 - px3)**2

    def compute_likelihood_using_contours(self, state):
        self.model.set_state([state])
        sum_ = 0.0
        normal = self.model.normal(0.0)
        for i in range(settings.num_likelihood_features):
            t = float(i) / float(settings.num_likelihood_features)
            pt = self.model.evaluate(t)
            sum_ += self.detect_edge(pt+origo, normal)
        return sum_

    def compute(self):
        self.img = self.load_image()
        self.debug_img = self.img.copy()
        self.model = model.Model()
        self.counter += 1
        weights = []
        for i in range(self.num_particles):
            weights.append(self.compute_likelihood_using_contours(self.particles[i]))
        tmp_img = Image.fromarray(numpy.uint8(self.debug_img))
        tmp_img.save(os.path.join(settings.tmp_dir, 'image%06d.png'%self.counter))
        return weights
        
