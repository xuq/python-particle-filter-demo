import os
import numpy

def mkdir(path, show_error = False, show_command = True):
    print('util.mkdir("%s")' % path)
    try:
        os.makedirs(path)
    except OSError as e:
        if show_error:
            print(e)

def rotate(angle):
    return numpy.array([[numpy.cos(angle), -numpy.sin(angle)], [numpy.sin(angle), numpy.cos(angle)]])
