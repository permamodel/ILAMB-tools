#!/usr/bin/env python
"""Symlinks model output files from ILAMBv1 to ILAMBv2."""

import os


src_dir = '/nas/data/ILAMB/MODELS/original'
dst_dir = '/nas/data/ilamb/MODELS'


for root, dirs, files in os.walk(src_dir):
    if len(files) == 0:
        model_name = os.path.basename(root)
        new_model_dir = os.path.join(dst_dir, model_name)
        os.mkdir(new_model_dir)  # mode isn't set properly
        os.chmod(new_model_dir, 0775)
        os.chdir(new_model_dir)
    else:
        for file in files:
            os.symlink(os.path.join(root, file), file)
