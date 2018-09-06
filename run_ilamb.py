"""Run the ILAMB component through PyMT."""

import sys
from pymt.components import ILAMB


def main():
    if len(sys.argv) == 2:
        bmi_cfg_file = sys.argv[1]
    else:
        bmi_cfg_file = 'bmi_ilamb.yaml'
    m = ILAMB()
    m.initialize(bmi_cfg_file)
    m.update()
    m.finalize()

if __name__ == '__main__':
    main()
