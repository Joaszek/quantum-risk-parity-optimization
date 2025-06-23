import pandas as pd
from risk_parity_optimizer import optimize
from return_calculator import calculate_log_returns

log_returns = calculate_log_returns()
window_size = 20
step = 5
results = []

for start in range(0, len(log_returns) - window_size, step):
    end = start + window_size
    window_data = log_returns.iloc[start:end]
    cov = window_data.cov().values
    result, _ = optimize()
    selected_assets = result.x
    results.append({
        "window_start": start,
        "window_end": end,
        "selected_assets": selected_assets.tolist(),
        "objective_value": result.fval
    })

df_results = pd.DataFrame(results)
df_results.to_csv("results/sliding_window_risk_parity.csv", index=False)