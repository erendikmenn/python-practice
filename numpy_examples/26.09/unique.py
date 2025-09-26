import numpy as np
import pandas as pd

exp = {
    "Sehirler" : ["İzmir","İzmir","İstanbul","Ankara","İzmir"]
}

df = pd.DataFrame(exp)

print(df["Sehirler"].unique())