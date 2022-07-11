#!/bin/sh
#pyUNIxMD
export PYTHONPATH=$PYTHONPATH:/projects/academic/cyberwksp21/Students/$USER/unixmd/src

#DFTB+
module load intel/20.2
module load intel-mpi/2020.2
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so

source /util/academic/intel/20.2/compilers_and_libraries_2020.2.254/linux/bin/compilervars.sh intel64
source /util/academic/intel/20.2/compilers_and_libraries_2020.2.254/linux/mpi/intel64/bin/mpivars.sh
