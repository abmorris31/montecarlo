import numpy as np
import math
import networkx as nx
from .BitString import BitString

class IsingHamiltonian:

    def __init__(self, G):
        self.G = G
        self.mu = np.zeros(self.G.number_of_nodes(), dtype=int) 
    
    def energy(self, bs: BitString):
        A = nx.adjacency_matrix(self.G).todense()
        s = []
        for n in bs.config:
            if n == 0:
                s.append(-1)
            else:
                s.append(1)

        skip = 0
        E = 0
        row = 0
        col = 0
        for i in A:
            col = skip
            for j in i[skip:]:
                E += j*s[row]*s[col]
                col += 1
            skip += 1
            row += 1
        
        for i in range(len(self.mu)):
            E += self.mu[i]*s[i]
        
        return(E)

    def set_mu(self, mus:np.array):
        self.mu = mus
        

    def compute_average_values(self, T: float):
        bs = BitString(self.G.number_of_nodes())
        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0
        k = 1.0
        beta = 1/(k*T)
        N = len(bs)
        for i in range(0,2**N+1):
            bs.set_integer_config(i)
            eng = IsingHamiltonian.energy(self, bs)
            p = np.exp(-beta * eng)
            m = bs.on() - bs.off()
            E += eng * p
            M += m * p
            EE += eng**2 * p
            MM += m**2 * p
            Z += np.exp(-beta * eng)
        E = E / Z
        M = M / Z
        EE = EE / Z
        MM = MM / Z
    
        HC = (EE - E**2) / T**2
        MS = (MM - M**2) / T
    
        return E, M, HC, MS