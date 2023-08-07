import ase 
import sys

from ase.io import read, write
from ase.io.vasp import write_vasp_xdatcar
from ase.io.netcdftrajectory import write_netcdftrajectory
from ase.io.proteindatabank import write_proteindatabank

for f in sys.argv[1:]:
    print(f + " => " + f"{f}.netcdf")
    t = ase.io.read(f, index=':')

    # Trajectory formats
    ase.io.vasp.write_vasp_xdatcar(f"{f}.xdatcar", t, label=None)
    ase.io.netcdftrajectory.write_netcdftrajectory(f"{f}.netcdf", t)
    ase.io.proteindatabank.write_proteindatabank(f"{f}.traj.pdb", t)

    # Single snapshots, sometimes required for atom type
    ase.io.vasp.write_vasp(f"{f}.poscar", t[0])
    ase.io.proteindatabank.write_proteindatabank(f"{f}.pdb", t[0])

