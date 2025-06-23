from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler
import numpy as np
from return_calculator import calculate_log_returns
from risk_parity_utils import compute_risk_parity_loss

def build_qubo(cov_matrix, num_assets):
    qp = QuadraticProgram()
    for i in range(num_assets):
        qp.binary_var(name=f"x{i}")

    linear = {}
    quadratic = {}
    for i in range(num_assets):
        for j in range(num_assets):
            key = (f"x{i}", f"x{j}")
            coeff = cov_matrix[i][j]
            if key in quadratic:
                quadratic[key] += coeff
            else:
                quadratic[key] = coeff
    qp.minimize(linear=linear, quadratic=quadratic)

    qp.linear_constraint(
        linear={f"x{i}": 1 for i in range(num_assets)},
        sense="==",
        rhs=2,
        name="select_2_assets"
    )
    return qp

def optimize():
    log_returns = calculate_log_returns()
    cov_matrix = np.cov(log_returns.T)
    n = log_returns.shape[1]

    qp = build_qubo(cov_matrix, n)
    sampler = Sampler()
    qaoa = QAOA(sampler=sampler, optimizer=COBYLA())
    optimizer = MinimumEigenOptimizer(qaoa)
    result = optimizer.solve(qp)

    return result, cov_matrix