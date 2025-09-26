import pandas as pd

exp = {
    "a": ["Test-1","Test-2"],
    "b": ["Test-3","Test-4"],
    "c": ["Test-5","Test-6"]
}

df = pd.Series(exp)

print(df.loc["b"])