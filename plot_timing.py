from matplotlib import pyplot
import settings
import cPickle as pickle

timing = pickle.load(open(settings.timing))

pyplot.figure()
pyplot.bar(range(len(timing)), timing, align='center')
pyplot.xticks(range(len(timing)), ['Dynamics', 'Observation', 'Multiply', 'Normalize', 'Num effective', 'Resampling'])
pyplot.ylabel('Time [s]')
pyplot.show()
#pyplot.savefig('/tmp/timing.pdf')
