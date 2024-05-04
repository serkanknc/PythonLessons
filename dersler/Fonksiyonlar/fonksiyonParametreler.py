#Parametrelerin Varsayılan Değerleri
#?Biz eğer bir parametrenin değerini varsayılan olarak belirlemek istersek, bunu varsayılan değerler ile yapabiliriz. 
#!Varsayılan değerleri anlamak için selamla fonksiyonunu varsayılan parametre değeri ile yazalım.

def selamla(isim = "İsimsiz"):
    print("Selam",isim)

selamla() # Hiç bir değer göndermedik. "isim" parametresinin değeri varsayılan olarak "İsimsiz" olarak belirlendi

def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)

bilgilerigöster() # Bütün parametreler varsayılan değerle ekrana basılacak.

bilgilerigöster("Mustafa Murat","Coşkun") # ad ve soyad değerini verdik ancak numara parametresi varsayılan değer oldu. 

#!Ancak böyle bir durumda argümanları gönderirken değerleri sıralı vermemiz gerekiyor. Peki sadece numara parametresine değer vermek istersek ne yapacağız ?

bilgilerigöster(numara = "123456") # numara parametresini özel olarak belirtiyoruz.

bilgilerigöster(ad = "Mustafa Murat",numara = "123456")

print("Mustafa","Murat","Coşkun",sep = "/") # sep parametresine özel olarak değer atadık.


#todo Biliyorsunuz bir fonksiyon yazıldığında özel olarak kaç tane parametresi olacağını önceden belirtmemiz gerekiyor. Örneğin, bir toplama fonksiyonu yazalım.

def toplama(a,b,c):
    print(a+b+c)

toplama(3,4,5,6) # 4 tane argüman veremeyiz.


#!Peki ben bir fonksiyonu esnek sayıda argümanla kullanmak istersem ne yapacağım ? Bunun için de Yıldızlı Parametre kullanmam gerekiyor. Kullanımı şu şekildedir;

def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam += i
    return toplam

print(toplama(3,4,5,6,7,8,9,10))

print(toplama())

#?print fonksiyonunu tekrar hatırlayacak olursak aslında print fonksiyonu bu şekilde tanımlanmış bir fonksiyondur. 
#*Çünkü biz print fonksiyonuna istediğimiz sayıda argüman gönderebiliyorduk.