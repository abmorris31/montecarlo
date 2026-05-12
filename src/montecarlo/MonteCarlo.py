import numpy as np
import random
import networkx as nx
from .BitString import BitString
from .IsingHamiltonian import IsingHamiltonian

class MonteCarlo:

    def __init__(self, ham):
        self.ham = ham
    
    def run(self,T,n_samples, n_burn):
        E_values = []
        M_values = []
        bs = BitString(self.ham.G.number_of_nodes())

        n = 0
        while n < n_samples:
            for i in range(len(bs)):
                E_a = IsingHamiltonian.energy(self.ham,bs)
                bs.flip_site(i)
                E_b = IsingHamiltonian.energy(self.ham,bs)
                if E_b <= E_a:
                    W = 1
                else:
                    W = np.exp(-(E_b - E_a)/T)
                
                if random.random() < W:
                    pass
                else:
                    bs.flip_site(i)
                    E_b = E_a

                n += 1
                if n > n_burn:
                    E_values.append(E_b)
                    M_values.append(bs.on() - bs.off())

        return E_values, M_values
        