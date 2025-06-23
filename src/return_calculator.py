import numpy as np
from data_loader import load_data

def calculate_log_returns():
    df = load_data()
    log_returns = np.log(df / df.shift(1)).dropna()
    return log_returns