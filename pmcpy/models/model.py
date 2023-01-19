import numpy as np

class Model:

    def __init__(self, eval_function, set_params):

        self._eval_function = eval_function
        self._set_params = set_params
        
    def __call__(self, X, params):

        self._set_params(params)
        
        return self._eval_function(X)



