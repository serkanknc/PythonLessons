#float() foknsiyonu int veri tipini float a dönüştürür

sayi = 24
print(float(sayi))

#int() fonksiyonu float veri tipini int a dönüştürür

sayi2 = 25.4
print(int(sayi2))

#str() fonksiyonu sayıları stringe çevirir

sayi3= 42423
donusumstring = str(sayi3)
print(donusumstring)
print(len(donusumstring))

#string ifadeleri tam sayıya çevirirken string her karakterininn bir rakam olması gerekmektedir int() fonksiyonu ile çevrilir

a = '4124123'
b = int(a)
print(b)

a = '41241sadsa123' # hatalı ifade
b = int(a)
print(b)


#string ifadeleri ondalık sayılara çevirirken string'in ondalık sayı ifadesine uygun olması gerekir float() fonksiyonu ile çevrilir.

c = "3.123145"
d= float(c)
print(d)

c = "3.123145.3232" # hatalı ifade
d= float(c)
print(d)