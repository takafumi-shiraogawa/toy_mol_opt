import numpy as np
import mol_opt as mo

# A toy code that performs geometry optimization
# of a diatomic molecule whose potential energy curve
# is described by the Morse potential

# Conversion factor from Angstrom to Bohr
ang_to_bohr = 1 / 0.52917721067

def calc_Morse(coord):
  """ Calculate Morse type potential energy

  Only for diatomic molecules

  """
  if len(coord) > 2:
    raise NotImplementedError("Read the code.")

  # parameters are fictioneous
  well_depth = 1.0
  well_width = 0.1
  eq_bond_length = 1.5

  bond_length = abs(coord[0, 2] - coord[1, 2])

  # Calculate energy
  energy = well_depth * ((1 - np.exp(-well_depth * (bond_length - eq_bond_length))) ** 2.0)

  # Calculate energy derivative with respect to the bond length
  deriv = 2 * well_depth * (1 - np.exp(-well_depth * (bond_length - eq_bond_length))) * \
    well_width * np.exp(-well_depth * (bond_length - eq_bond_length))

  return energy, deriv


if __name__ == "__main__":
  # Set parameters
  max_opt_num = 10000
  opt_criterion = 0.00005

  # diatomic molecule
  mol_coord = np.zeros((2, 3))
  mol_deriv = np.zeros((2, 3))

  # Set an initial bond length
  mol_coord[1, 2] = 1.0

  print("step, energy (Ha), drivative (Ha/Ang), bond length (Ang)")

  # Start geometry optimization
  for i in range(max_opt_num):
    energy, deriv = calc_Morse(mol_coord)
    mol_deriv[1, 2] = deriv
    mol_coord = mo.line_searcher.steepest_descent(mol_coord, mol_deriv / ang_to_bohr)
    print(i, energy, deriv, mol_coord[1, 2])
    if (abs(deriv) < opt_criterion):
      print("***********************************************")
      print(" Geometry optimization successfully terminated!")
      print(" Optimized bond length is ", mol_coord[1, 2], "Angstrom")
      print("***********************************************")
      break

  if i == max_opt_num - 1:
    print("***********************************************")
    print(" Geometry optimization failed!")
    print("***********************************************")