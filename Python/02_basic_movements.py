#liste oluşturmak için genelde [] ve list fonk kullanılır.

liste = ["a","b","c"]

type(liste)
liste = ["a",1,0.2]

liste[0]

liste1 = [1,2,3,4,5,6]
liste2 = ["a","b","c"]
liste_tum = [liste1, liste2]


#eleman işlemleri

fis = "ali uzaya git"

fis[0:4]

fis[1:3]

fis[1:]

liste = ["a",1,789,[11,22,33]]

yeni_liste = liste[3]

yeni_liste[2]

for i in yeni_liste:
    print(i*2)
    
    
    
    
liste = ["ali","veli","isik","ayse","berkcan"]

liste[0]="alinin babasi"

del liste[0]

liste = ["ali","veli","isik"]

liste.append("berkcan")
    
liste.insert(len(liste),"berkcan")

liste
    
# =============================================================================
# # Tuple OLUŞTURMA
# =============================================================================

#üstünde değişiklik yapilamaz
#
#sözlükler

sozluk = {"reg" : "regresyon modeli",
          "loj" : "lojistik regresyon",
          "cart" : "classification and regression trees"}

sozluk2 = {"reg" : 10,
           "loj" : 11,
           "cart" : 12}

sozluk3 = {"reg" : ["RMSE", 10],
           "loj" : ["MSE",11],
           "cart" : ["SSE",12]}



#eleman


sozluk["reg"]

sozluk["gbm"] = "gradient boosting machines"

sozluk











# =============================================================================
# #KÜMELER
# =============================================================================

s = set()

type(s)

l = [1,"a","b",123]

s = set(l)

ali = "ali lutfen ata bakmayi kes"

s = set(ali)

s #küme olacak şekilde bastı

#değerleri çoklama durumunda tek basar


set1 = set([4,6,8])
set2 = set([4,5,6])


set1.symmetric_difference(set2)
