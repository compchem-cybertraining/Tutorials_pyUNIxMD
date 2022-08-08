from __future__ import division
from qm.model.model import Model
import numpy as np

class Tully(Model):
    """ Class for simple avoided crossing (SAC) model BO calculation
    
        :param object molecule: molecule object
        :param double A: parameter for simple avoided crossing model
        :param double B: parameter for simple avoided crossing model
        :param double C: parameter for simple avoided crossing model
        :param double D: parameter for simple avoided crossing model
    """
    def __init__(self, molecule, A=0.01, B=1.6, C=0.005, D=1.):
        # Initialize model common variables
        super(Tully, self).__init__(None)
        
        # Define parameters
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
        # Set 'l_nacme' with respect to the computational method
        # SAC model can produce NACs, so we do not need to get NACME
        molecule.l_nacme = False
        
        # SAC model can compute the gradient of several states simultaneously
        self.re_calc = False
     
    def get_data(self, molecule, base_dir, bo_list, dt, istep, calc_force_only):
        """ Extract energy, gradient and nonadiabatic couplings from simple avoided crossing model BO calculation
       
            :param object molecule: molecule object
            :param string base_dir: base directory
            :param integer,list bo_list: list of BO states for BO calculation
            :param double dt: time interval
            :param integer istep: current MD step
            :param boolean calc_force_only: logical to decide whether calculate force only
        """
        # Initialize diabatic Hamiltonian
        H = np.zeros((2, 2))
        dH = np.zeros((2, 2))
        U = np.zeros((2, 2))
        
        x = molecule.pos[0]
        
        # Define Hamiltonian
        
        # Define a derivative of Hamiltonian
        
        # Diagonalization
        
        # Extract adiabatic quantities
        molecule.states[0].energy =
        molecule.states[1].energy =
        
        molecule.states[0].force =
        molecule.states[1].force =
        
        molecule.nac[0, 1, 0, 0] =
        molecule.nac[1, 0, 0, 0] =

