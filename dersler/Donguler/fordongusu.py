#in Operatörü
#Pythondaki in operatörü , bir elemanın başka bir listede,demette veya stringte (karakter dizileri) bulunup bulunmadığını kontrol eder. Kullanımı şu şekildedir;

#"a" in "merhaba"
#True

#for Döngüsü
#for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin üzerinde dolaşmamızı sağlayan bir döngü türüdür. Yapısı şu şekildedir.

#for eleman in veri_yapısı(liste,demet vs):
#            Yapılacak İşlemler

liste = [1,2,3,4,5,6,7]

for eleman in liste:
    print("Eleman",eleman)

# Liste elemanlarını toplama
liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam",toplam)

s =  "Python"
for karakter in s:
    print(karakter)

# Listelerle aynı mantık
demet =  (1,2,3,4,5,6,7)

for eleman in demet:
    print(eleman)


# Listelerin içinde 2 boyutlu demetler
liste = [(1,2),(3,4),(5,6),(7,8)]

for eleman in liste:
    print(eleman) # Herbir elemanın  demet olduğu görebiliyoruz.

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]

for (i,j) in liste:
    print(i,j)

# Metodları kullanmadan sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük:
    print(eleman)

    # keys() - Aynı şey
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük.keys():
    print(eleman)

    # values() 
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük.values():
    print(eleman)


    # items() 
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for (i,j) in sözlük.items():
    print("Anahtar:",i,"Değer:",j)