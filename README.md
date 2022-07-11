Tutorials for the pyUNIxMD code
===============================
This repository is for containing hands-on materials for pyUNIxMD.
1. demo_pyunixmd_dftb: nonadiabatic dynamics using pyUNIxMD with DFTB+ for CNH4+ and PSB3 molecules
2. add_a_new_model: a DIY example to add a model qm object to pyUNIxMD

To try these hands-on tutorials, you need to install the pyUNIxMD package [J. Comput. Chem. 2021, 42, 1755-1766] and set environment for DFTB+[J. Chem. Phys. 2020, 152, 124101].

Installation of pyUNIxMD
------------------------
You can install pyUNIxMD from its Github page.

``` bash
$ git clone https://github.com/skmin-lab/unixmd.git
```

Activate pyunixmd conda environment by
``` bash
$ conda activate pyunixmd
```

Go to the pyUNIxMD root directory and compile the C codes. Time-consuming calculations such as electronic evolution are done with C functions through Cython package.
``` bash
$ cd ./unixmd
$ python setup.py build_ext -b ./src/build
```

Setting for DFTB+
-----------------
There's a bash script for setting environment variables.
``` bash
$ cd ..
$ cp /projects/academic/cyberwksp21/Students/dhan/set_pyunixmd_dftb.sh .
$ source set_pyunixmd_dftb.sh
```

The content of the shell script is
``` bash
#!/bin/sh
#pyUNIxMD
export PYTHONPATH=$PYTHONPATH:/projects/academic/cyberwksp21/Students/$USER/unixmd/src

#DFTB+
module load intel/20.2
module load intel-mpi/2020.2
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so

source /util/academic/intel/20.2/compilers_and_libraries_2020.2.254/linux/bin/compilervars.sh intel64
source /util/academic/intel/20.2/compilers_and_libraries_2020.2.254/linux/mpi/intel64/bin/mpivars.sh
```
You may want to change the PYTHONPATH if your project directory name is different from your account name.

About NAC calculations
----------------------
The TD-DFTB implementation of DFTB+ cannot give NACV, so NACs are calculated by a finite difference method [J. Phys. Chem. Lett. 2015, 6, 21, 4200–4203] using a time-delayed overlap matrix in pyUNIxMD. To get the overlap matrix, a doubled-molecule technique is used in pyUNIxMD. However, after DFTB+ v20.2, DFTB+ checks the input geometry if there is a pair of atoms too close each other and if any, the calculation halts. Thus, the corresponding part of the code is needed to be commented out, which is in the updateNeighbourList subroutine at $dftbplus/prog/dftb+/lib_dftb/periodic.F90.
``` Fortran
    ! check for atoms on top of each other
    do iAtom1 = 1, nAtom
      do nn1 = 1, neigh%nNeighbour(iAtom1)
        if (neigh%neighDist2(nn1, iAtom1) < minNeighDist) then
          iAtom2 = img2CentCell(neigh%iNeighbour(nn1, iAtom1))
          write (strError, "(A,I0,A,I0,A)") "Atoms ",iAtom1, " and ", iAtom2, " too close together"
          call error(strError)
        end if
      end do
    end do
  end subroutine updateNeighbourList
```




