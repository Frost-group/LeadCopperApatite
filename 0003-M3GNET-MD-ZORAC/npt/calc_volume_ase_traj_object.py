from ase.io import read,Trajectory
import sys

dt = 0.020  # Time step in traj files 
traj = Trajectory(sys.argv[1])

time = [ i*dt for i in range(len(traj)) ]
volume = [ atoms.get_volume() for atoms in traj ]

for t,v in zip(time,volume):
    print(t," ",v)


