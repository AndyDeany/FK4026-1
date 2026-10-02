"""
Module for solving the 1D Helmholtz equation using Finite Differences.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


def build_matrix(n: int, h: float, k: float) -> sp.csr_matrix:
    """
    Constructs the sparse finite difference matrix for the discrete system:
        -u'' - k^2 u = f
    with boundary conditions:
        u(0) = 0  (Dirichlet)
        u'(1) = i*k*u(1)  (absorbing boundary condition via backward difference)
    """
    # Main diagonal entries: 2/h^2 - k^2
    main_diag = np.full(n, 2. * h ** -2 - k ** 2, dtype=complex)

    # Off-diagonal entries: -1/h^2
    sub_diag = np.full(n - 1, - h ** -2, dtype=complex)
    super_diag = np.full(n - 1, - h ** -2, dtype=complex)

    # Dirichlet boundary at x = 0 (grid index 0): set row to identity
    main_diag[0] = 1.0
    super_diag[0] = 0.0

    # Robin boundary at x = L (grid index n-1):
    # Backward difference for u'(1) -> (u_{n-1} - u_{n-2})/h = i*k*u_{n-1}
    # Matrix row: (-1/h) * u_{n-2} + (1/h - i*k) * u_{n-1} = 0
    main_diag[-1] = h ** -1 - 1j * k
    sub_diag[-1] = - h ** -1

    # Construct tridiagonal matrix
    diagonals = [sub_diag, main_diag, super_diag]
    offsets = [-1, 0, 1]
    matrix = sp.diags(diagonals, offsets, shape=(n, n), format='csr')

    return matrix


def build_rhs(x_grid: np.ndarray, k: float) -> np.ndarray:
    """
    Constructs the right-hand side vector for the linear system.
    """
    mean, sigma = .3, .1
    rescaling = - k ** 2 / ((2 * np.pi) ** .5 * sigma)
    exponential = np.exp(1j * k * x_grid)
    b = rescaling * exponential * np.exp(-2 * ((x_grid - mean) / sigma) ** 2)
    b[0] = b[-1] = 0.  # fix boundary conditions
    return b


def solve_helmholtz(k: float, L: float = 2 * np.pi, num_nodes: int = 1000) -> tuple[np.ndarray, np.ndarray, float]:
    """
    Solves the 1D Helmholtz boundary value problem using a finite-difference scheme:
        -u''(x) - k^2 * u(x) = - k^2 * f(x) * g(x),   x in (0, L)
    The forcing term f is a Gaussian with:
        mean    x = 0.3
        std sigma = 0.1
    The forcing term g is a complex exponential:
        g(x) = exp(1j * k * x)
    The boundary conditions are:
        u(0) = 0                    (Dirichlet condition)
        u'(L) = i * k * u(L)        (absorbing Robin condition)

    Parameters
    ----------
    k : float
        Wavenumber (k > 0).
    L : float, optional
        Length of the spatial domain (default is 2*PI).
    num_nodes : int, optional
        Number of grid points including boundaries (default is 1000).

    Returns
    -------
    x_grid : np.ndarray
        1D array of spatial coordinates along the domain [0, L].
    u : np.ndarray
        Complex-valued array representing the numerical solution field u(x).
        Each entry x_i of x_grid corresponds to the solution value u_i=u(x_i) in u.
    norm : float
        Discrete L2 norm of the wave field calculated over the spatial grid:
            norm = sqrt(h * sum_i(|u_i|^2))
        where h is the grid spacing (h = x_grid[1] - x_grid[0]).

    Examples
    --------
    >>> import helmholtz_fd
    >>> x, u, norm = helmholtz_fd.solve_helmholtz(k=5.0)
    >>> print("Number of grid points:", len(x), "Solution norm:", norm)
    """
    x_grid = np.linspace(0.0, L, num_nodes)
    h = x_grid[1] - x_grid[0]

    # Assemble and solve sparse linear system A * u = b
    A = build_matrix(num_nodes, h, k)
    b = build_rhs(x_grid, k)
    u = spla.spsolve(A, b)

    # Compute discrete L2 norm using vectorized norm calculation
    norm = float(np.sqrt(h) * np.linalg.norm(u))

    return x_grid, u, norm
