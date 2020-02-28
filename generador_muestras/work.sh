#!/bin/bash                                                                                                                                                    
#SBATCH --nodes=1                                                                                                                                              
#SBATCH --ntasks-per-node=10                                                                                                                                   
#SBATCH --job-name=serial_test                                                                                                                                 
#SBATCH --time=168:0:0                                                                                                                                          
#SBATCH --partition=general                                                                                                                                    
#SBATCH --constraint=broadwell                                                                                                                                 

srun python genera.py -event=100000 -dirmad="/LUSTRE/home/fmsanchez/MG5_aMC_v2_7_0/"
