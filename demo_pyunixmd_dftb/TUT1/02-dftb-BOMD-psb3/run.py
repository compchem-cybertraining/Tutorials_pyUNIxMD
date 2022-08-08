from molecule import Molecule
from thermostat import NHC
import qm, mqc
from misc import data, au_to_K

# Define the target system.
geom = """
14

C  -6.03587491  -0.72724403  -0.07930056  0.000  0.000  0.000 
C  -4.64636042  -0.79047511   0.02007315  0.000  0.000  0.000
H  -6.60209445   0.21157016  -0.14998244  0.000  0.000  0.000
H  -6.59071045  -1.68495200  -0.07153981  0.000  0.000  0.000
H  -4.01935646  -1.71045587   0.01820167  0.000  0.000  0.000
C  -3.91312207   0.42219465   0.01752045  0.000  0.000  0.000
C  -2.57817158   0.51198598   0.10303206  0.000  0.000  0.000
H  -4.41274348   1.44294978   0.01894382  0.000  0.000  0.000
H  -1.89724913  -0.41133355   0.22289777  0.000  0.000  0.000
C  -1.80490692   1.72682263   0.07272271  0.000  0.000  0.000
H  -2.37056222   2.69439715   0.11464634  0.000  0.000  0.000
N  -0.56698508   1.78633368   0.20660982  0.000  0.000  0.000
H  -0.04889533   2.75713893   0.18906629  0.000  0.000  0.000
H  -0.00460531   0.89460878   0.20309725  0.000  0.000  0.000
"""
mol = Molecule(geometry=geom, nstates=1, charge=+1.)

# Set QM method.
qm = qm.dftbplus.DFTB(molecule=mol, version="20.1", install_path="/user/username/_install_dftb_20.1/", sk_path="/user/username/mio-1-1/")

thermo = NHC(time_scale = 10.0, temperature=300.)

# Determine MD method.
md = mqc.BOMD(molecule=mol, thermostat=thermo, nsteps=5000, dt=0.5, istate=0)

# Execute the simulation.
md.run(qm=qm)
