import numpy as np


class SMC:

    def __init__(self, mutator, particles):

        self._mutator = mutator
        self._particles = particles
    
    def sample(self, model, smc_steps, 
                                    ess_threshold=0.75):
        
        

        

