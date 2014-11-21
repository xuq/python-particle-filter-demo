from matplotlib import pyplot
import settings
import cPickle as pickle

source_data = pickle.load(open(settings.source_data))
theta_ref = source_data['theta_ref']
theta = pickle.load(open(settings.result))

pyplot.figure(figsize=(8,2))
pyplot.plot(range(len(theta_ref)), theta_ref)
pyplot.hold(True)
pyplot.plot(range(len(theta)), theta)
pyplot.ylabel('Angle [theta]')
#pyplot.show()
pyplot.savefig('plot.pdf')
