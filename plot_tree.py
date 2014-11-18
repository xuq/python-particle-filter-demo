import settings
import cPickle as pickle
from matplotlib import pyplot
import utils
import os

utils.mkdir(settings.pf_tree_dir)

# Matplotlib is quickly bogged down, so we plot the tree sequentially and merge at the end.

tree = pickle.load(open(settings.pf_tree))
theta_ref = pickle.load(open(settings.source_data))['theta_ref']

fig = pyplot.figure()
pyplot.plot(range(len(theta_ref)), theta_ref, 'g', zorder=2, linewidth=3.0)
pyplot.ylim([-1.5, 1.5])
pyplot.xlim([0, len(theta_ref)-1])
pyplot.ylabel('Angle [rad]')
pyplot.savefig(os.path.join(settings.pf_tree_dir, 'theta_ref.png'))
pyplot.close()

for n, tr in enumerate(tree):
    fig = pyplot.figure()
    pyplot.gca().get_yaxis().set_visible(False)
    pyplot.gca().get_xaxis().set_visible(False)

    pyplot.ylim([-1.5, 1.5])
    pyplot.xlim([0, len(theta_ref)-1])
    pyplot.hold(True)
    for before, after in zip(*tr):
        x = [n, n+1]
        y = [before, after]
        pyplot.plot(x, y, 'b', zorder=1)
    pyplot.savefig(os.path.join(settings.pf_tree_dir, 'image%06d.png'%n), transparent=True)
    print(n)
    pyplot.close()

# Imagemagick for composition of images

src1 = os.path.join(settings.pf_tree_dir, 'image%06d.png' % 0)
src2 = os.path.join(settings.pf_tree_dir, 'theta_ref.png')
dst = os.path.join(settings.pf_tree_dir, 'image%06d.png' % 0)
cmd = 'composite %s %s %s' % (src1, src2, dst)
print(cmd)
os.system(cmd)

for n in range(len(theta_ref)-1):
    src1 = os.path.join(settings.pf_tree_dir, 'image%06d.png'%(n+1))
    src2 = os.path.join(settings.pf_tree_dir, 'image%06d.png'%n)
    dst = os.path.join(settings.pf_tree_dir, 'image%06d.png'%(n+1))
    cmd = 'composite %s %s %s' % (src1, src2, dst)
    print(cmd)
    os.system(cmd)
