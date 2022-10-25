## A toy code that performs geometry optimization
## of a diatomic molecule whose potential energy curve
## is described by the Morse potential.

### Model & Method
The molecule is modeled based on the Moarse potential. All the
parameters are given in test_Morse.py. mol_opt.py is a module
for the steepest descent optimization. The internal coordinate
is used, which means that the bond length is a geometry parameter
to be optimized.

### Usage
The geometry optimization of the molecule can be performed using
the following command:
`$ python3 test_Morse.py`
The result can be checked by calculating the potential energy
curve:
`$ python3 calc_PES.py`