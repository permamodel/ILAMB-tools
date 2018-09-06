#! /usr/bin/env bash
#PBS -N ILAMB
#PBS -M mark.piper@colorado.edu
#PBS -m e
#PBS -l pmem=8gb
#PBS -l nodes=1:ppn=2
#PBS -l walltime=12:00:00

cd $PBS_O_WORKDIR
source /home/csdms/wmt/_testing/conda/bin/activate
export PYTHONPATH=$PWD
python run_bmiilamb.py MsTMIP.bmi.yaml
