import pandas as pd
import os

df = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")
df2 = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")

print(df['Id'].dtypes)

