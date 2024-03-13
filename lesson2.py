# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:31:14 2024

@author: lenovo
"""

isim = "Zeynep"
print(isim[0])   # 'Z'
print(isim[5])   # 'p'

print(isim[-1])  # 'p'
# print(isim[-10])  # IndexError: string index out of range
print(isim[-10])  # 'Z' (ilk karakter)

a = "Python Programlama"

print(a[0])        # 'P'
print(a[2:8])      # 'thon P'
print(a[0:18])     # 'Python Programlama'
print(a[:])        # 'Python Programlama'

print(a[:12])      # 'Python Progr'
print(a[5:])       # 'n Programlama'

print(a[17])       # 'a'
print(a[0:17])     # 'Python Programlam'

print(a[-10:-2])   # 'rogramla'

print(a[0:15:2])   # 'Pto rgam'
print(a[::2])      # 'Pto rgmla'
print(a[::3])      # 'Ph oa'

print(a[::-1])     # 'amalmargorP nohtyP'
print(isim[::-1])  # 'penyeZ'

x = "Merhaba"
y = "Dünya"

print(x + y)       # 'MerhabaDünya'
print(x * 3)       # 'MerhabaMerhabaMerhaba'

# print(x + 3)    # TypeError: can only concatenate str (not "int") to str
# print(x - 3)    # TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print(x / 6)    # TypeError: unsupported operand type(s) for /: 'str' and 'int'

"""
Yorum
satırları
"""

"""
Değişken isimleri
*  sayı ile başlamasın
*  kelimeler ile arasında boşluk olmasın
*  :'",><?!()@#$%^&*-+~  kullanılmaz (_) alt tire kullanılır
*  Kodlayama özel kelimeleri kullanma (true, no, do)
"""

sayi1 = 20
# 1sayi = 12  # SyntaxError: invalid syntax

ogrNo = 111
# ogr no = 111  # SyntaxError: invalid syntax

# while = 10   # SyntaxError: invalid syntax

print(9 + 8)   # 17
print(9 - 5)   # 4
print(5 * 8)   # 40
print(98 // 5) # 19
print(98 % 5)  # 3

sayi1 = 20
sayi2 = 10

# 1. yol
# gecici = sayi1
# sayi1 = sayi2
# sayi2 = gecici

# 2. yol
sayi1, sayi2 = sayi2, sayi1

sayi1 = sayi1 + 1
sayi1 += 1
# sayi1++  # Hatalı

print("Merhaba")
print("Merhaba", "Dünya")
print("Merhaba", 1, 2, 3)
print("Merhaba", 1, 2, 3, 5.5, 6.2, 4.8)

print("Merhaba\nDünya")    # Enter
print("Merhaba \tDünya")   # Tab -> boşluk+\t

print("""
      Merhaba
      Arkadaşlar
      Nasılsınız""")

print("""
      Merhaba
Arkadaşlar
      Nasılsınız""")

# print("
#       Merhaba
# Arkadaşlar
#       Nasılsınız")

# type fonksiyonu
a = 55
print(type(a))
b = 45.78
print(type(b))
c = "Merhaba"
print(type(c))
d = 'a'
print(type(d))

# sep parametresi

print(1, 2, 3, 4, 5, sep=".")
print(1, 2, 3, 4, 5, sep=",")
print(1, 2, 3, 4, 5, sep=", ")

print(7, 3, 2024, sep=".")
print(7, 3, 2024, sep="/")

print(18, 31, sep=":")
print(18, 31, 30, sep=":")

print("ocak", "şubat", "mart", sep=",")
print("ocak", "şubat", "mart", sep="\n")
print("ocak", "şubat", "mart", sep="\t")

print(*"zeynep")
print(*"zeynep", sep="\n")

print(*"TBMM", sep=".")

# formatlama
x = 5
y = 10

print("{} + {} = {}".format(x, y, x + y))

print("{}  {}  {}".format(7, 3, 2024))
print("{0}  {1}  {2}".format(7, 3, 2024))

print("{1}  {0}  {2}".format(7, 3, 2024))
print("{2}  {1}  {0}".format(7, 3, 2024))

print("{} {} {}".format(3.458796, 4.5462, 5.546))
print("{:.4f} {:.3f} {:.2f}".format(3.458796, 4.5462, 5.546))

# Liste
liste = [1, 2, 3, 4, 5]
print(liste)
print(type(liste))

liste2 = ["a", "b", "c"]
print(liste2)

liste3 = ["merhaba", "dünya"]
print(liste3)

liste4 = [1, 2, 3, "merhaba", 4.5]
print(liste4)

# boşliste

bosliste = []
bosliste2 = list()

# liste boyutu
print(len(liste4))

s = "zeynep"
liste5 = list(s)
print(liste5)

# liste5[0]
# liste5[5]
# liste5[10]

print(liste5[-1])
# print(liste5[-10])  # IndexError: list index out of range

# listenın son elemanı
print(liste5[-1])
print(liste5[len(liste5) - 1])

# listenın ilk elemanı
print(liste5[0])
print(liste5[-len(liste5)])

print(liste







