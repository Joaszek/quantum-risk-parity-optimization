# 🧠 Quantum Risk Parity Optimization with Sliding Windows

This project demonstrates how to apply the **Quantum Approximate Optimization Algorithm (QAOA)** to perform **risk parity-based portfolio optimization** using real financial data in a **sliding window** approach.

It simulates dynamic investment decisions by selecting subsets of assets where **each asset contributes equally to portfolio risk**, using a quantum-inspired method. The model runs over time windows to reflect real-world rebalancing behavior.

---

## 📊 Problem Setup

We solve a constrained binary optimization problem aiming to achieve **risk parity** — equal risk contributions from selected assets.

The risk parity imbalance is minimized by building a **QUBO** from the covariance matrix of asset returns.

**Objective**  
Minimize risk contribution imbalance using:  
contributions = weights · Σ → target = mean(contributions)  
loss = ∑(contributions - target)²

**subject to**  
∑xᵢ = k, xᵢ ∈ {0,1}

Where:
- (xᵢ): whether asset *i* is selected  
- (Σ): covariance matrix  
- (k): number of assets to select (e.g., 2)

The problem is solved using:
- `Qiskit Optimization` (`QuadraticProgram`)
- `QAOA` from `qiskit-algorithms`
- `MinimumEigenOptimizer`

---

## 🔁 Sliding Window Approach

The optimizer runs over **20-day windows** of log returns, moving every **5 days**. For each window, a risk parity portfolio is calculated and results are tracked over time.

---

## 📁 Folder Structure

```bash
project/
│
├── data/
│   └── data_apple_cocacola_google.csv        # Raw price data
│
├── results/
│   └── sliding_window_risk_parity.csv        # Optimizer output per window
│
├── plots/
│   └── risk_parity_objective_over_time.png   # Visualization of objective values
│
├── src/
│   ├── data_loader.py                        # Loads CSV price data
│   ├── return_calculator.py                  # Computes log returns
│   ├── risk_parity_utils.py                  # Computes risk contributions & loss
│   ├── risk_parity_optimizer.py              # Builds and solves QUBO with QAOA
│   ├── window_optimizer.py                   # Sliding window optimization loop
│   └── plot_results.py                       # Plots objective values
