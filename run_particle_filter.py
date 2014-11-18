import sir
import dynamics
import observation_model
import cPickle as pickle
import settings
import utils

if __name__ == '__main__':
    utils.mkdir(settings.results_dir)
    utils.mkdir(settings.posterior_dir)

    data = pickle.load(open(settings.source_data))

    obs_model = observation_model.ObservationModel()
    dyn_model = dynamics.Dynamics()

    pf = sir.Sir(settings.num_particles, settings.N_thr, settings.state_dim, obs_model, dyn_model)
    theta = []
    posterior = []

    for n in range(settings.num_images):
        print(n)
        pf.step()
        theta.append(pf.mean[0])
        posterior.append(zip(pf.weights.copy(), pf.particles.copy()))

    pickle.dump(theta, open(settings.result, 'w'))
    pickle.dump(posterior, open(settings.posterior, 'w'))
    pickle.dump(pf.timing, open(settings.timing, 'w'))
    pickle.dump(pf.tree, open(settings.pf_tree, 'w'))
        
