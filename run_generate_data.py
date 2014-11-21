import utils
import draw
import model
import numpy
import cPickle as pickle
import settings
import os

origo = numpy.array(settings.origo)

def reference_dynamics(t):
    return 0.7 * numpy.sin(0.1*t)

def make_image_pyplot(n,  theta):
    from matplotlib import pyplot
    fig = pyplot.figure()
    m = model.Model()
    m.set_state(theta)
    pyplot.hold(True)
    for line in m.lines:
        pyplot.plot([line.start[0], line.end[0]], [line.start[1], line.end[1]], linewidth=4.0, color='black')
    circ = pyplot.Circle(m.ball, 15.0, color='r', zorder=2)
    fig.gca().add_artist(circ)
    pyplot.xlim([-240, 240])
    pyplot.ylim([-240, 240])
    fig.savefig(os.path.join(settings.source_image_dir, 'image%06d.pdf'%n), transparent=True)
    

def make_image(n, theta):
    fig = draw.Draw()
    m = model.Model()
    m.set_state(theta)
    for line in m.lines:
        fig.plot(origo + line.start, origo + line.end)
    fig.circle(origo + m.ball, 15.0)
    fig.save(os.path.join(settings.source_image_dir, 'image%06d.png'%n))
    
if __name__ == '__main__':
    utils.mkdir(settings.source_image_dir)
    theta_ref = []
    
    for n in range(settings.num_images):
        theta = reference_dynamics(n)
        theta_ref.append(theta)
#        make_image_pyplot(n, [theta])
        make_image(n, [theta])
        print(n)

    data = {'theta_ref' : theta_ref}
    pickle.dump(data, open(settings.source_data, 'w'))

