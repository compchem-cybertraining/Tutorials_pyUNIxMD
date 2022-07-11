from molecule import Molecule
from thermostat import NHC
import qm, mqc
from misc import data, au_to_K

# Define the target system.
with open("geom.xyz", "r") as fp:
    geom = fp.read()
mol = Molecule(geometry=geom, nstates=3, charge=+1)

# Set QM method.
qm = qm.dftbplus.DFTB(molecule=mol, version="20.1", install_path="/home/dhhan/program/_install_dftb_20.1/", sk_path="/home/dhhan/program/slko/mio-1-1/")

thermo = NHC(time_scale = 3.0, temperature=300.)

# Determine MD method.
md = mqc.SHXF(molecule=mol, thermostat=thermo, nsteps=120, nesteps=1000, dt=0.25, istate=2, elec_object="density", hop_rescale="energy", hop_reject="keep", sigma=0.07)

# Execute the simulation.
md.run(qm=qm)
