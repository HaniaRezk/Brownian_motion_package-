import numpy as np
from .base_pygm import Simulator

class GBMSimulator(Simulator):
    def __init__(self,y,mu,sigma):
        super().__init__(y,mu,sigma)


    def simulate_path(self,T,N):
        dt = T / N
        t_values = np.linspace(0, T, N + 1)
        y_values = np.zeros(N + 1)
        y_values[0] = self.y
        for i in range(1, N + 1):
            dB = np.sqrt(dt) * np.random.normal()
            y_values[i] = self.y * np.exp((self.mu - 0.5 * self.sigma**2) * dt + self.sigma * dB)
        return t_values, y_values
        
        
