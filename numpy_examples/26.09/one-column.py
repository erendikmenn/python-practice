import pandas as pd

exp = {
    "İsim":["Can","Ece","Ada"],
    "Puan":[85,92,78]
}

df = pd.Series(exp)

print(df["İsim"])