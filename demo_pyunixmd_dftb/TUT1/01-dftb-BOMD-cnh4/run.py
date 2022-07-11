from molecule import Molecule
from thermostat import NHC
import qm, mqc
from misc import data, au_to_K

# Define the target system.
geom = """
6

C  -0.04474383   0.02851832   0.04519326   0.000 0.000 0.000  
N  -0.04441695  -0.06449170   1.27599013   0.000 0.000 0.000
H   0.89522209  -0.03575664  -0.51205651   0.000 0.000 0.000
H   0.88084838  -0.07197904   1.86478714   0.000 0.000 0.000
H  -0.81785945   0.01033355   1.81981263   0.000 0.000 0.000
H  -1.02074371  -0.01600249  -0.55063563   0.000 0.000 0.000
"""
mol = Molecule(geometry=geom, nstates=1, charge=+1.)

# Set QM method.
qm = qm.dftbplus.DFTB(molecule=mol, version="20.1", install_path="/user/username/_install_dftb_20.1/", sk_path="/user/username/mio-1-1/")

thermo = NHC(time_scale = 10.0, temperature=300.)

# Determine MD method.
md = mqc.BOMD(molecule=mol, thermostat=thermo, nsteps=50000, dt=0.5, istate=0)

# Execute the simulation.
md.run(qm=qm)
