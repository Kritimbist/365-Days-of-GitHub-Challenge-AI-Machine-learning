import numpy as np
import pandas as pd

sensor_a = pd.DataFrame({
    "time":[1,2,3,4,5],
    "temperature":[22.0,23.5,np.nan,26.0,28.7]
})
sensor_b =pd.DataFrame({
    "time":[1,2,3,4,5],
    "temperature":[21.8,23.7,26.5,37.9,29.9]
})

#Merge datasets
merged = pd.merge(sensor_a,sensor_b,on="time",suffixes=("_A","_B"))

# Data Fusion
#fuse by taking average
merged["fused_temperature"]= merged[
    ["temperature_A","temperature_B"]
].mean(axis=1)
print(merged[["time", "fused_temperature"]])
