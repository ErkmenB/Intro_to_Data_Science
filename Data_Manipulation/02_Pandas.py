import pandas as pd
import numpy as np

# mesele matris işlemleri değil yeğen mesele veri analizi
# işin matematik optimizasyon hesaplama kısmı numpy
# işin modelleme makine öğrenmesi veri görselleştirme pandasda
# pandas numpyın alternatifi değil numpyın özelliklerini kullanan ve bunları genişleten bir kütüphanedir.

### Pandas Series 

seri = pd.Series([1,2,3,4])           #pandasın farkı index yapısıyla seri oluşturması
type(seri)

seri.values
seri.head(2)
seri[0:3]

### Numpy arrayi üzeerinden pandas serisi oluşturmak 

a = np.array([1,2,3,566,88])
seri = pd.Series(a)
seri
seri[0]

pd.Series([1,5,0.9,34],index = [1,3,5,7])
seri = pd.Series([1,5,0.9,34],index = ['a','b','c','d'])
seri['a']

### Sozluk üzerinden pandas seri 

sozluk = {"reg":10,"loj":11,"cart":12}
sozluk

seri = pd.Series(sozluk)
seri["reg":"cart"]
seri

pd.concat([seri,seri])
seri.append(seri)
seri

### Serilerde Eleman İşlemleri 

a = np.array([1,2,3,33,55,66])
seri = pd.Series(a)
seri

seri = pd.Series([121,200,150,99], index = ["reg","loj","cart","rf"])
seri
seri.keys()

"knn" in seri           #elimizde bir sürü veri olduğunda spesifik veriler için sorgu yapabiliriz.
"reg" in seri

seri["rf"] = 125
seri["rf"]

seri = pd.Series([121,200,150,99], index = ["reg","loj","cart","rf"])
seri

seri[(seri>125) & (seri <200)]

### Serilerde index problemi 

data = pd.Series(["a","b","c"], index = [1,3,5])
data
data[1]           #Dikkat edilmesi gereken bir nokta. Elimizde 0 diye bir index yok. Ona gitmeye çalışırssak hata alırız.
data[1:3]         #slicing işleminde ise aralık verdiğimiz için 1 indexini görmezden geldi

# loc label based indexing, tanımlandığı şekil ile index yakalamak

data.loc[0:2]    #normalde 2. indexe kadar getirmesini bekleriz.
                #Ama dataframe mantığında anca 2 indexli değer varsa getirir yoksa getirmez
data.iloc[0]    #pozisyonel indeks alışık olduğumuz gibi çekiyoruz

## Pandas DataFrame Özellikler ve Oluşturma 

l = [1,4,577,343]
l
df = pd.DataFrame(l, columns = ["degisken_ismi"])
df
df.shape

a = np.array([1,2,3,4,56])
pd.DataFrame(a, columns = ["degisken ismi"])

m = np.arange(1,10).reshape(3,3)
m

df = pd.DataFrame(m,columns =["var1","var2","var3"])
df

df.columns = ("deg1","deg2","deg3")
df

pd.DataFrame(m,columns = ["var1","var2","var3"], index = ["a","b","c"])
a = pd.Series([1,2,3,4])
pd.DataFrame(a,columns = ["degisken"])

bir = pd.Series([1,2,3,4])
iki = pd.Series([1,2,3,4])

pd.DataFrame({"degisken1": bir, "degisken2":iki})



