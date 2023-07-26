from __future__ import annotations

import warnings

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from pymatgen.core import Lattice, Structure
from pymatgen.io.ase import AseAtomsAdaptor

import matgl
from matgl.ext.ase import M3GNetCalculator, MolecularDynamics, Relaxer

import ase

# To suppress warnings for clearer output
warnings.simplefilter("ignore")


pot = matgl.load_model("M3GNet-MP-2021.2.8-PES")

ase_adaptor = AseAtomsAdaptor()
# Create ase atom object
#
#atoms = ase_adaptor.get_atoms(final_structure)
atoms = ase.io.read("P6Pb9Cu1O26H2.vasp")

# Initialize the velocity according to Maxwell Boltzamnn distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
# Create the MD class
driver = MolecularDynamics(atoms, potential=pot, 
                           temperature=300, timestep=1.0, 
                           ensemble="nvt",
                           trajectory="md.traj", logfile="md.log")
# Run
driver.run(1000)


