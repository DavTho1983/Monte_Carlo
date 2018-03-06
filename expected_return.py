import numpy as np
import pandas as pd

roi = np.array([0.04, 0.08, 0.11])
p = np.array([0.3, 0.4, 0.3])
df = pd.DataFrame([roi, p], index=['roi', 'probability'])

def expected_return(df):
    exp_rets_array = []
    for i in range(len(df.columns)):
        temp_values_array = np.array(df[i])
        total = np.prod(temp_values_array)
        exp_rets_array.append(total)
    exp_rets_array = np.asarray(exp_rets_array)
    exp_rets_df = pd.DataFrame([exp_rets_array], index=['E[r]'])
    df = df.append(exp_rets_df)
    return df

print(expected_return(df))
