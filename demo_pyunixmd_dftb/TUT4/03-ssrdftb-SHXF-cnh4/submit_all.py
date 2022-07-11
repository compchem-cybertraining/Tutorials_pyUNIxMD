import os
import shutil

ntrajs = 5

for itraj in range(ntrajs):
   dir_traj = f"TRAJ_{itraj + 1:03d}/"
   shutil.copy("submit.sh", dir_traj)
   os.chdir(dir_traj)
   os.system("sbatch submit.sh")
   os.chdir("..")
