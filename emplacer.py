#!/usr/bin/env python
"""Puts MsTMIP output files in a standardized location for ILAMB.

Examples
--------
Copy all the `ra` files from *transfer* to the appropriate MsTMIP
directories in *MODELS/original* with:

$ python emplacer.py

"""

import os
import shutil
import glob
import string


ILAMB_dir = '/nas/data/ILAMB'
transfer_dir = os.path.join(ILAMB_dir, 'transfer')
models_dir = os.path.join(ILAMB_dir, 'MODELS', 'original')

model_list = [
    'BIOME-BGC',
    'CLASS-CTEM-N',
    'CLM4',
    'CLM4VIC',
    'DLEM',
    'GTEC',
    'ISAM',
    'LPJ-wsl',
    'ORCHIDEE-LSCE',
    'SiB3',
    'SiBCASA',
    'TEM6',
    'TRIPLEX-GHG',
    'VEGAS2.1',
    'VISIT',
]

mstmip_variable = 'rh'
mip_table = 'Lmon'

for model in model_list:
    try:
        pattern = string.join([mstmip_variable, mip_table, model, '*'], '_')
        transfer_file_list = glob.glob(os.path.join(transfer_dir, pattern))
        transfer_file = transfer_file_list.pop()
        print '\nTransfer:', transfer_file
        os.chmod(transfer_file, 0664)
    except IndexError:
        print '\nVariable {}, MIP {}, not matched to model {}.'.format(
            mstmip_variable, mip_table, model)
    else:
        mstmip_variable_dir = os.path.join(models_dir, model, mstmip_variable)
        print 'Destination:', mstmip_variable_dir
        os.mkdir(mstmip_variable_dir)  # mode isn't set properly
        os.chmod(mstmip_variable_dir, 0775)
        shutil.copy(transfer_file, mstmip_variable_dir)
