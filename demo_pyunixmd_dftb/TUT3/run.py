from molecule import Molecule
import qm

install_path = "/user/username/_install_dftb_20.1/"
mio_path = "/user/username/mio-1-1/"
ob2_path = "/user/username/ob2-1-1/base/"

# Define the target system.
geom = """
6
planar CNH4 
C     0.000000     0.000000     0.000000     0.000000     0.000000     0.000000
N     0.000000     0.000000     1.335000     0.000000     0.000000     0.000000
H     0.943102     0.000000    -0.544500     0.000000     0.000000     0.000000
H     0.943102     0.000000     1.879500     0.000000     0.000000     0.000000
H    -0.943102     0.000000     1.879500     0.000000     0.000000     0.000000
H    -0.926647     0.000000    -0.535000     0.000000     0.000000     0.000000
"""
mol = Molecule(geometry=geom, nstates=2, charge=+1)

# Functions to perform dftb+ and print energies
def calc_dftb(qm, mol):
    qm.write_xyz(mol); qm.get_input(mol, -1, [0], False)
    qm.run_QM(mol, "./", -1, [0], False); qm.extract_QM(mol, "./", -1, [0], 1., False)
    print(f"{mol.states[0].energy:13.8f} {mol.states[1].energy:13.8f}", end="") 

def calc_ssr(qm, mol):
    qm.write_xyz(mol); qm.get_input(mol, -1, [0], False)
    qm.run_QM("./", -1, [0]); qm.extract_QM(mol, [0], False)
    print(f"{mol.states[0].energy:13.8f} {mol.states[1].energy:13.8f}", end="") 

# Investigate S0, S1 PES by rotating the molecule
import numpy as np
def rmat_z(theta):
    Rz = np.array([np.cos(theta), -np.sin(theta), 0., np.sin(theta), np.cos(theta), 0., 0., 0., 1.])
    Rz = Rz.reshape((3,3))
    return Rz
deg2rad = np.pi/180; da = 5.; rz = rmat_z(da*deg2rad)

for ir in range(36):
    print(f"{ir*da} ", end="")

    # Set QM method.
    qm1 = qm.dftbplus.DFTB(molecule=mol, version="20.1", install_path=install_path, sk_path=mio_path); qm1.calc_coupling=False
    qm2 = qm.dftbplus.SSR(molecule=mol, version="20.1", install_path=install_path, sk_path=ob2_path, l_range_sep=True, tuning = [3.0, 3.0, 3.0]); qm2.calc_coupling=False
    calc_dftb(qm1, mol)
    calc_ssr(qm2, mol)
    print("")
   
    # Rotating the molecule 
    mol.pos[3] = np.dot(rz, mol.pos[3])
    mol.pos[4] = np.dot(rz, mol.pos[4])
     
