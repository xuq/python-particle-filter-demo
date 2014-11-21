import os
import numpy

base_dir         = '/tmp/pendulum'
source_image_dir = os.path.join(base_dir,         'source')
source_data      = os.path.join(source_image_dir, 'data.dump')
tmp_dir          = os.path.join(base_dir,         'tmp')
results_dir      = os.path.join(base_dir,         'results')
result           = os.path.join(results_dir,      'theta.dump')
histogram_dir    = os.path.join(base_dir,         'histogram')
prior_dir        = os.path.join(base_dir,         'prior')
likelihood_dir   = os.path.join(base_dir,         'likelihood')
posterior_dir    = os.path.join(base_dir,         'posterior')
posterior        = os.path.join(posterior_dir,    'data.dump')
timing           = os.path.join(results_dir,      'timing.dump')
pf_tree_dir      = os.path.join(base_dir,         'pf_tree')
pf_tree          = os.path.join(results_dir,      'pf_tree.dump')

num_particles = 1000
# Threshold for resampling
N_thr = num_particles / 2

state_dim = 1
num_likelihood_features = 16
num_images = 500

# Origin of image
origo = 225, -220

# Size of image
width, height = 450, 450

image_color_mode = 'L'
#image_color_mode = 'RGB'

def noise_func():
    return 0.5 * (numpy.random.rand(1) - 0.5)

def initialization_func():
    return numpy.linspace(-numpy.pi, numpy.pi, num_particles)
