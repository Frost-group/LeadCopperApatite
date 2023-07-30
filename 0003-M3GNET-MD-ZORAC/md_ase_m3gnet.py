from __future__ import annotations


import warnings
warnings.simplefilter("ignore")


# Specify device before imports or code runs
import torch
torch.set_default_device("cuda")


from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

import matgl
from matgl.ext.ase import MolecularDynamics

import sys
import ase

f = sys.argv[1]
atoms = ase.io.read(f)

# Convert model to `cuda` 
pot = matgl.load_model("M3GNet-MP-2021.2.8-PES").to("cuda")

# Initialize the velocity according to Maxwell Boltzamnn distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Create the MD class
driver = MolecularDynamics(
    atoms,
    potential=pot,
    temperature=300,
    timestep=1.0,
    ensemble="nvt",
    loginterval=20,
    trajectory=f"{f}_md.traj",
    logfile=f"{f}_md.log",
)
# Run
driver.run(100000)
# 1000 steps (1ps) takes around 2' on Zorac
