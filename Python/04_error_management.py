#hata yönetimi


A = 1 
B = 0


A/B


try:
    print(A/B)
except ZeroDivisionError:
    print("Paydada sıfır olur mu? ")

a = 1 
b = "2"

a/b


try: 
    print(a/b)
except TypeError:
    print("Sayı girersen daha güzel olur.")



try: 
    print(int(a)/int(b))
except TypeError:
    print("Sayı girersen daha güzel olur.")

