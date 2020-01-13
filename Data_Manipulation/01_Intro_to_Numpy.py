# Kodlar interaktif bir şekilde çalışmanın eseridir. Bir Bütünlük aranmamalıdır.

# Numerical Python
# Çok boyutlu arraylerle ilgili yüksek performanslı çalışma imkanı sağlar.

import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

L = [1,2,"a",1.2]
L

# Python listeleri çok fazla yer kaplıyor.
# Numpyın en büyük avantajlarından biri güzel bir optimizasyon sağlaması.

### Listelerden Array Oluşturmak

import numpy as np

a = np.array([12,33,4,5])
type(a)

np.zeros(10,dtype = int)
np.ones((2,3))
np.full((2,3),9)
np.linspace(0,1,30)
np.random.normal(0,1,(3,4))
np.eye(3)

### Yeniden biçimlendirme

np.arange(1,10).reshape((3,3))
a = np.array([1,2,3])
a.reshape((1,3))
a[: , np.newaxis]

x = np.array([1,2,3])
y = np.array([4,5,6])
z = [1,2,3]
np.concatenate([x,y,z])

a = np.array([[1,2,3],
            [4,5,6]])
a
np.concatenate([a,a])

np.concatenate([a,a] , axis = 1)
a = np.array([1,2,3])
b = np.array([[9,8,7],
            [6,5,4]])
a, b

### boyutları birbirleriyle örtüşmeyen arrayleri birleştirdik 

np.vstack([a,b]) 
a = np.array([[99],[99]])
np.hstack([a,b])

### Ayırma İşlemleri 

x = [1,2,3,99,99,3,2,1]
x
np.split(x,[3,5,6,7])

a,b,c,d,e = np.split(x,[3,5,6,7])
a

m = np.arange(16).reshape((4,4))
m

np.vsplit(m,[2])

ust, alt = np.vsplit(m,[2])
ust

### Array Sıralama 

v = np.array([2,1,4,3,5])
v
np.sort(v)

i = np.argsort(v)  
i

np.array([3.14,4,6,1.2])

## NumPy eleman işlemleri 

a = np.random.randint(10,size =(3,5))
a

a[0,0] = 1
a[0,0]

a = np.arange(20,30)
a
a[0::2]

a = np.random.randint(10,size = (5,5))
a

a[:,0]    # : koyulduğunda yerinde olması gereken değer seçilmiş gibi oluyor

a[0:2,0:3]

a = np.random.randint(10,size = (5,5))
a

alt_a = a[0:3,0:2]

alt_a

alt_a[0,0] = 9999
alt_a[1,1] = 9999
alt_a

a            #Bu durum büyük veri setlerinde küçük bi alt küme seçip onun üstünde yaptığımız değişiklikler ile ana küme hakkında işlem yapabilmek aadına
             # önemli bi durum
              
# eğer bu şekilde değişmesini istemiyorsak bunu pythona anlatmalıyız. Bunu da .copy() ile yaparız.

alt_b = a[0:3,0:2].copy()
alt_b


alt_b[0,0] = 9999
alt_b[1,1] = 9999

a          #burada değerler değişmeyecek. çünkü b yi atarken copy() ile belirttik.

### Fancy İndex İşlemleri  

v = np.arange(0,30,3)
v

[v[1], v[3]]

al_getir = [1,3,5]
v[al_getir]

m = np.arange(9).reshape(3,3)
m

satir = np.array([0,1])
sutun = np.array([1,2])
m[satir,sutun]

m[0,[1,2]]
m[0:,[1,2]]

v = np.arange(10)
v

index = np.array([0,1,2])
index

v[index]
v[index] = 99
v

### Koşullu Eleman İşlemleri 

v = np.array([1,2,3,4,5])
v > 3

#### İki Arrayi karşılaştırma 

v*2
(v**2)
(v*2) == (v**2)
v = np.random.randint(0,10,(3,3))
v
v > 5
np.sum(v > 5)
np.sum((v>3) & (v < 7))

####  Satır ve sütun bazında sorgulama

np.sum(v > 4, axis = 1)
np.all(v > 4)   # tüm elemanlar 4ten büyük mü değil mi
np.any(v >5)
v = np.array([1,2,3,4,5])

## NumPy Hesaplamalı işlemler 

a = np.arange(5)
a*2
a**5

np.add(a,2)
np.subtract(a,1)
np.multiply(a,3)
np.power(a,3)

a = np.arange(1,6)
a
np.add.reduce(a)
np.add.accumulate(a)

a = np.random.normal(0,1,30)
a
np.mean(a)
np.std(a)
np.var(a)
np.median(a)

## Farklı Boyutlu Arraylerle Birlikte Çalışmak 


a = np.array([1,2,3])
b = np.array([1,2,3])

a+b

m = np.ones((3,3))
m

a+m    #hepsine tek tek ekledi
a = np.arange(3)
a

b = np.arange(3)[:, np.newaxis]
b       

a+b

m = np.ones((2,3))
m

a = np.arange(3)
a

a + m

a = np.arange(3).reshape((3,1))
a

b = np.arange(3)
b

a.shape
b.shape

a+b

m = np.ones((3,2))
m
a = np.arange(3)
a
a+m     #broadcast problemi

# numpy ortaya çıkışı itibariyle tek tip verilerle çalışmak üzere tasarlanmıştır.
# karışık iç içe operasyonlarda koşullar döndürmek istediğimizde numpy bize cevap veremez.
# pandas a geçiyoruz.

m = np.ones((3,3))
m[:,1]

m[0:,[1,2]]

m = np.arange(16).reshape((4,4))
m

m = np.arange(16).reshape((4,4))
m[0:,]
