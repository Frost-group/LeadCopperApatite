from __future__ import annotations

import warnings

import sys

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from pymatgen.core import Lattice, Structure
from pymatgen.io.ase import AseAtomsAdaptor

import matgl
from matgl.ext.ase import M3GNetCalculator, MolecularDynamics, Relaxer

import ase

# To suppress warnings for clearer output
warnings.simplefilter("ignore")


pot = matgl.load_model("M3GNet-MP-2021.2.8-PES")

f=sys.argv[1]
atoms = ase.io.read(f)

# Initialize the velocity according to Maxwell Boltzamnn distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
# Create the MD class
driver = MolecularDynamics(atoms, potential=pot, 
                           temperature=300, timestep=1.0, 
                           ensemble="npt",
                            pressure=1,
                            compressibility_au = 16.66,
                           loginterval=20, trajectory=f"{f}_md.traj", 
                           logfile=f"{f}_md.log")
# bulk modulus estimated as in Ev/A^3 = 0.06 (10 GPa), invert this to get compressiiblity
# I think this must be using a Bernendsen thermo + baro stat?

# Run
driver.run(100000)
# 1000 steps (1ps) takes around 2' on Zorac; on the unit cell

