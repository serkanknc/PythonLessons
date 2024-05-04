
#? enumerate fonksiyonunu daha iyi anlamak için ilk önce şu örneğe bakalım.

liste = ["Elma","Armut","Muz","Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuç = list()

i = 0

for a in liste:
    
    sonuç.append((i,a))
    i +=1
print(sonuç)

# aslında burada herbir elemanı indekslerle numaralandırıyor ve demet çiftleri oluşturuyoruz. 
#* for döngüsü yazarken bazen hem elemanları hem de indeksleri almak isteyebiliriz. 
#* Böyle bir durumda numaralandırma işlemi yapan enumerate fonksiyonunu kullanabiliriz.

liste = ["Elma","Armut","Muz","Kiraz"]
list(enumerate(liste))



#* çift sayıdaki indekslerin elemanlarını yazdırdık
liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ",eleman)
    


#todo örnek

isimler = ["Alice", "Bob", "Charlie"]

# enumerate fonksiyonu kullanarak indeks ve değeri al
for indeks, isim in enumerate(isimler):
    print(f"{indeks + 1}. kişi: {isim}")

#enumerate, for döngülerinde çoğu zaman işlerimizi oldukça kolaylaştırmaktadır. 