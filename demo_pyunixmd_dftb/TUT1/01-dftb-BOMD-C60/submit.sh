#!/bin/sh
#SBATCH --account=alexeyak
#SBATCH --job-name=pyunixmd
#SBATCH --partition=valhalla  --qos=valhalla
#SBATCH --clusters=faculty
#SBATCH --time=360:30:00
#SBATCH --nodes=8
#SBATCH --mem=5000
#SBATCH --ntasks-per-node=16

# Set the nr. threads for dftb-omp

start_time=`date +%s`i

echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NODELIST="$SLURM_JOB_NODELIST
echo "SLURM_NNODES="$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR
echo "working directory="$SLURM_SUBMIT_DIR


export OMP_NUM_THREADS=1

# Set a scratch directory
export SCRADIR=/panasas/scratch/grp-cyberwksp21/qingxin/dyn_$SLURM_JOB_ID

mkdir $SCRADIR

cp $SLURM_SUBMIT_DIR/* $SCRADIR 
ln -s $SCRADIR ./SCRADIR
cd $SCRADIR

python run.py >log

cp * $SLURM_SUBMIT_DIR
cp -r md/ $SLURM_SUBMIT_DIR
end_time=`date +%s`
echo execution time was `expr $end_time - $start_time` s.
rm -rf $SCRADIR
