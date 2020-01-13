## Gözlem ve Değişkenlere Birlikte Erişmek 

# Gözlem ve değişkenlerin ikisine de slice işlemiyle ulaşmaya çalışırsak hata yaşayabiliriz.
# loc ve iloc yapılarını kullanmak daha mantıklı. 
# Eğer oluşturulan indexe sağdık bir şekilde bir seçim işlemi yapılacaksa loc kullanıyorduk. 
# Eğer indexleri alışık olduğumuz şekilde positional şeklinde seçmek istiyorsak iloc yapısı kullanıyorduk. 

import pandas as pd
import numpy as np

s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

df = pd.DataFrame({"var1":s1, "var2":s2, "var3":s3})
df

df.loc[0:3]            #normalde 3ü almasını beklemezdik ama loc ifadesi indexlere sağdık kalır. 
df.iloc[0:3]         # ilocda ise alışık olduğumuz şekilde 3 e kadar olarak algılar ve 3 ü bastırmaz

df.iloc[0,0]
df.iloc[:3,:2]
df.iloc[2:6,1:3]

df.loc[0:3, 'var3']
df.loc[0:3, 'var2':'var3']  #iki tarafta da slicing yaparsak 'str yaapısı ile' iloc kullanamayız hata verir mecbur loc

df.iloc[0:3,'var2':'var3']
df.iloc[0:3, 1:3]       # bu yapıda da eğer str kullanmayacaksak iloc seçmeliyiz. loc hata verir.

df.loc[:3,1:3]    # görüldüğü üzere ikisi de hata verdi. loc iloc kullanımına dikkat edilmeli.

df.index = ["a","b","c","d","e"]
df

df.loc["c":"d", "var2":"var3"]
df

df[df.var1 > 5]
df[df.var1 > 5]['var2']   #sadece var1 in 5 ten büyük olduğu koşulu sağlayan var2 değerlerini aldık.
df[(df.var1 >5) & (df.var3 < 7)]  # bu şekilde koşulları paranteze alıp & ile bağlarsak birden fazla koşul aratabiliriz.

df.loc[df.var1 > 5 ,['var2','var1']]