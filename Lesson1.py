# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:48:59 2024

@author: lenovo
"""

# Merhaba Dünya yazdırma
print("Hello World")

# İki string'i birleştirme
x = "Merhaba"
y = "Dünya"
print(x + y)

# Sayılarla işlem yapma
a = 10
b = 5.2

# Sayıları farklı türler arasında dönüştürme
c = float(a)
d = int(b)

# Değişkenleri ekrana yazdırma
print(c)
print(d)

# Sayıları dönüştürerek ekrana yazdırma
print(float(15))
print(int(10.5))
print(int(10.9))
print(int(10.1))

# Sayıyı stringe dönüştürme
e = 4578
f = str(e)
print(f)

# String uzunluğunu yazdırma (hatalı, çünkü len() fonksiyonu sadece stringlerde çalışır)
# len(e)  # hatalı
# len(12547)
# len(f)

# Sayıyı stringe çevirme ve uzunluğunu yazdırma
g = 45.45
i = str(g)
print(i)
len(i)

# Stringi sayıya dönüştürme
a = "12345"
b = int(a)
print(b)

# Hatalı dönüştürme işlemleri (ValueError)
# c = "asdasfs"
# d = int(c)
# e = "45.45asd"
# f = float(e)

# Matematiksel Operatörler
x = 23
y = 6
z = 12

# Toplama, çıkarma, çarpma, bölme
print(x + y)
print(x - y)
print(x * y)
print(z / y)  # her zaman float olur

# Tam bölme, mod alma
print(x / y)
print(x // y)
print(x % y)

# Kuvvet alma, karekök
print(z ** y)
print(2 ** 3)
print(5 ** 2)
print(25 ** 0.5)

# Negatif sayı
print(-z)

# İşlem önceliği
print(9 + 5 // 2 - 1 * 3)
print(5**4/2)
print(8/4**3)
print(11 % 3 * 2)

# Stringler
print("Merhaba")
print('Merhaba')
print("""Merhaba""")

# Çok satırlı string
print("""   Merhaba 
      Dünya""")

# Tek tırnak içinde string (çift tırnak içinde de olabilir)
print("Bandırma'da hava çok sisli")

# String içindeki karakterlere erişme
isim = "Zeynep"
print(isim[0])
print(isim[5])
# print(isim[10])  # Hatalı

# Tersten karakterlere erişme
print(isim[-1])
# print(isim[-6])  # Hatalı
