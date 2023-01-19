from .particles import Particles

import numpy as np

class Mutator:

    def __init__(self, mcmc, mcmc_steps):

        self._mcmc = mcmc
        self._mcmc_steps = mcmc_steps


    def __call__(self, model, particles, phi):

        params, likelihood = self._mcmc(particles, model, 
                                        self._mcmc_steps, phi)
        
        mutated_particles = particles.create_new_particles(params, likelihood)

        return mutated_particles
