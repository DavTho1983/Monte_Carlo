import numpy as np
import pandas as pd

roi = np.array([0.12, 0.05, -0.1])
p = np.array([0.4, 0.5, 0.1])
df = pd.DataFrame([roi, p], index=['roi', 'probability'])

def e_r(df):
    """Calculate expected returns"""
    exp_rets_array = []
    for i in range(len(df.columns)):
        temp_values_array = np.array(df[i])
        total = np.prod(temp_values_array)
        exp_rets_array.append(total)
    exp_rets_array = np.asarray(exp_rets_array)
    exp_rets_df = pd.DataFrame([exp_rets_array], index=['E[r]'])
    df = df.append(exp_rets_df)
    std = std_r(df)
    return (df, std)

def std_r(df):
    """Calculate standard deviation of E[r]"""
    # mean = ((0.04 + 0.08 + 0.11) / 3)
    # std = (((0.04**2)*0.3) + ((0.08**2)*0.4) + ((0.11**2)*0.3) - (mean**2))**0.5
    e_r_var = 0
    e_r_mean = np.sum(df.loc['E[r]'])
    # print(e_r_mean)
    for i in range(len(df.columns)):
        e_r_val = df.iloc[0, i]
        # print(df.iloc[0, i])
        # print(df.iloc[1, i])
        val = ((df.iloc[0, i] - e_r_mean)**2) * df.iloc[1, i]
        # print(val)
        e_r_var += val
    # print(e_r_var)
    # print(e_r_mean)
    e_r_std = (e_r_var)**0.5
    return e_r_std

print(e_r(df))
