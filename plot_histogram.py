from matplotlib import pyplot
import settings
import cPickle as pickle
import os
import numpy

posterior = pickle.load(open(settings.posterior))
data = pickle.load(open(settings.source_data))
theta_ref = data['theta_ref']

for i in range(settings.num_images):
    
    w,p = zip(*posterior[i])

    pyplot.figure()
    n, bins, patches = pyplot.hist(p, 60, normed=True)
    pyplot.xlim([-2*numpy.pi, 2*numpy.pi])
    pyplot.ylim([0.0, 3.0])
    pyplot.hold(True)
    pyplot.plot([theta_ref[i], theta_ref[i]], [0.0, 3.0], linewidth=4.0)
    pyplot.xlabel('Angle [rad]')
    pyplot.savefig(os.path.join(settings.posterior_dir, 'image%06d.png' % i))
    pyplot.close()
    print(i)

