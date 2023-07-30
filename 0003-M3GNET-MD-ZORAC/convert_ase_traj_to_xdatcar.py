import ase
import sys

from ase.io import read, write
from ase.io.vasp import write_vasp_xdatcar

for f in sys.argv[1:]:
    print(f + " => " + f"{f}.xdatcar")
    t = ase.io.read(f, index=":")
    ase.io.vasp.write_vasp_xdatcar(f"{f}.xdatcar", t, label=None)
