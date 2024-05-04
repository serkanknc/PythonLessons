
#?Bu konuda zip fonksiyonu öğrenmeye çalışacağız. 
#zip fonksiyonunu öğrenmeden önceden liste elemanlarını gruplamaya çalışalım ve daha sonrasında zip fonksiyonunun faydasını görmeye çalışalım.

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i],liste2[i]))
    
    i +=1
print(sonuç)


#! böyle uzun bir işlemi zip fonksiyonuyla nasıl yaparız ? İsterseniz zip fonksiyonunun kullanımını direk örnek üzerinden görelim.

list(zip(liste1,liste2))

#* Burada zip fonksiyonunun kullanımını görüyoruz. zip fonksiyonu listelerin elemanları sırasıyla demet şeklinde gruplayarak bir tane liste oluşturuyor. Başka bir örnek yapalım.

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Python","Php","Java","Javascript","C"]

list(zip(liste1,liste2,liste3))

## Aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)


# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.

list(zip(sözlük1.values(),sözlük2.values())) # Değerler eşleşti

#örnek
isimler = ["Alice", "Bob", "Charlie"]
yaslar = [25, 30, 35]
meslekler = ["Mühendis", "Öğretmen", "Doktor"]

# isimler, yaslar ve meslekleri birleştirerek tuple'ları içeren bir liste oluştur
bilgiler = list(zip(isimler, yaslar, meslekler))

# Sonucu ekrana yazdır
for bilgi in bilgiler:
    print(bilgi)