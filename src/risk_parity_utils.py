import numpy as np

def compute_risk_contributions(weights, covariance_matrix):
    portfolio_volatility = np.sqrt(weights @ covariance_matrix @ weights.T)
    marginal_contributions = covariance_matrix @ weights
    risk_contributions = weights * marginal_contributions / portfolio_volatility
    return risk_contributions

def compute_risk_parity_loss(weights, covariance_matrix):
    contributions = compute_risk_contributions(weights, covariance_matrix)
    target = np.mean(contributions)
    loss = np.sum((contributions - target) ** 2)
    return loss