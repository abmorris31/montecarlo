import numpy as np
import math       


class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        count = 0
        for i in self.config:
            if i == 1:
                count += 1
        return count

        """
        Return number of bits that are on
        """

    def off(self):
        count = 0
        for i in self.config:
            if i == 0:
                count += 1
        return count
        """
        Return number of bits that are off
        """

    def flip_site(self,i):
        if self.config[i] == 1:
            self.config[i] = 0
        else:
            self.config[i] = 1
        """
        Flip the bit at site i
        """
    
    def integer(self):
        integer = 0
        n = len(self.config) - 1
        for i in self.config:
            if i == 1:
                integer += pow(2,n)
            n -= 1
        return integer
        """
        Return the decimal integer corresponding to BitString
        """
 

    def set_config(self, s:list[int]):
        self.config = s
        """
        Set the config from a list of integers
        """

    def set_integer_config(self, dec:int):
        index = len(self.config)-1
        for i in self.config:
            if dec % 2 == 1:
                self.config[index] = 1
            else:
                self.config[index] = 0
            dec = dec // 2
            index -= 1
        return self.config

        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """