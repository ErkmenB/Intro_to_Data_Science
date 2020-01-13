## DataFrame Eleman İşlemleri 

import pandas as pd
import numpy as np

s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

df = pd.DataFrame({"var1":s1, "var2":s2, "var3":s3})
df
df[0:1]

df.index = ["a","b","c","d","e"]
df

df["c":"e"]
df.drop("b")

## inplace olmadan kaydedilmez !!!!!!!!!!!!!!11 

df.drop("a",inplace=True)
df

"var1" in df
df.var1

df[["var1","var2"]]                 #Bunu alışkanlık edinmek çok daha faydalı

df["var4"] = df["var1"]/df["var2"]
df


