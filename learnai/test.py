import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv', sep='#', index_col=0)
print("DF", df)

df.boxplot(column = ['Glucose'], by=['Outcome'])
plt.xlabel('Diabetic Condition')
plt.ylabel('Glucose Level')
# plt.show()

bins = [0, 80, 90, 120, 200]
bin_labels = ['Normal', 'High Blood Pressure 1', 'High Blood Pressure 2', 'Hypertensive']
bp_status = pd.cut(df.BloodPressure, bins=bins).value_counts()
bp_status.index = bin_labels
#print(bp_status)

df_new_features = pd.DataFrame(data={
    'patient_id': [30, 430, 259, 103, 525],
    'BMI': [34.1, 35.0, 25.9, 22.5, 31.6],
    'Age': [38, 43, 24, 21, 24]
})


combined = df.join(
    df_new_features, on='patient_id'
).sort_values(by=['Age', 'BMI'])
print('COMB', combined)

combined_filtered = combined.loc[combined.Age <= 65].sort_index()
print('FILT', combined_filtered)

