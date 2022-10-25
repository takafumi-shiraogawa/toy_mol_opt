import numpy as np

# Conversion factor from Angstrom to Bohr
ang_to_bohr = 1 / 0.52917721067

class line_searcher():
  """ Perform line searches for sequential optimization methods."""

  # Perform a line search by a steepest descent minimization manner
  def steepest_descent(coord, gradient, grad_scale_factor = 0.1):
    """ Calculates the updated molecular geometry.

		Args:
			coordinates:		A (N, 3) array of nuclear coordinates [Angstrom]
      gradient:      A (N, 3) array of derivative of objective function with respect to given nuclear coordinates [Hartree / Bohr]
			grad_scale_factor:			A conventional scale factor of gradients
		Returns:
			next_coord: A (N, 3) array of updated nuclear coordinates [Angstrom]
		"""
    next_coord = np.zeros((len(coord), 3))
    for i in range(len(coord)):
      next_coord[i] = coord[i] - (grad_scale_factor * gradient[i] * ang_to_bohr)

    return next_coord