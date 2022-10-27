ENV["PYTHON"] = "/usr/local/bin/python"
using PyCall # to use pycall
using Base
using Printf

# Add the current directory to path
if PyVector(pyimport("sys")["path"])[1] != ""
  pushfirst!(PyVector(pyimport("sys")["path"]), "")
end
pyMorse = pyimport("test_Morse")

# mol_coord = Array{Float16}(undef, 2, 3)
mol_coord = zeros(Float64, 2, 3)

# Please care the structure of the array.
# It starts from 1 similar to Fortran, not to Python.
mol_coord[2, 3] = 0.5

for i = 1:200
  mol_coord[2, 3] += 0.05
  # println(mol_coord[2, 3], pyMorse.calc_Morse(mol_coord))
  @printf("%f %f %f\n", mol_coord[2, 3], collect(pyMorse.calc_Morse(mol_coord))...)
end