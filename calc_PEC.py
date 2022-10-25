import numpy as np
import test_Morse as tm

# Check the potential energy curve

mol_coord = np.zeros((2, 3))
mol_coord[1, 2] = 0.5

print("bond length (Ang), energy (Ha), drivative (Ha/Ang)")
for i in range(200):
  mol_coord[1, 2] += 0.05
  print(mol_coord[1, 2], *tm.calc_Morse(mol_coord))