import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/sliding_window_risk_parity.csv")
plt.figure(figsize=(10, 6))
plt.plot(df["window_end"], df["objective_value"], marker='o')
plt.title("Risk Parity QAOA Optimization Over Time")
plt.xlabel("Window End")
plt.ylabel("QAOA Objective Value")
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/risk_parity_objective_over_time.png")
plt.show()