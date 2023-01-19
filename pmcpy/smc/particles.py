import numpy as np

class Particles:

    def __init__(self, model, priors, parallel=1, particles=None, 
                        proposal=None, log_likes=None, log_weights=None):
        
        self._model
        self._priors = priors
        self._parallel = parallel

        if proposal == None:
            self._initialize_particles_from_priors(particles)
        
        else:
            self._intialize_particles_from_proposal(proposal)
        
        if log_likes == None:
            self._log_likes = self._model.compute_log_likes(self._params)
        else:
            self._log_likes = log_likes

        if log_weights == None:
            self._log_weights = self._model.compute_log_weights(self._params)
        else:
            self._log_weights = log_weights


    def _initialize_particles_from_priors(self, particles):
        
        params = np.empty((self._parallel, particles, len(self.priors)))

        for prior in self.priors:
            
            params[:,:,i] = prior.rvs(self._parallel*particles
                                    ).reshape((self._parallel, particles))
    
    self._params = params


    def _initialize_particles_from_proposal(self, proposal):
        
        if proposal.shape !==\
                (self._parallel, particles, len(self.priors)):
            raise ValueError("proposal dimensions should be " + \
                        f"({self._parallel, particles, len(self._priors)})")

        self._params = proposal
    
    def _new_particles(self, params, likelihood):

        return Particles(self._model, self._priors, parallel=self._parallel,
                        particles=params, log_likes=)
