
#İç içe Fonksiyonlar ve Fonksiyon Parametreleri

#? *args ve **kwargs

def fonksiyon(*args): # İstediğimiz sayıda argüman gönderebiliyoruz.
    print(args)
    for i in args:
        print(i)
fonksiyon(1,2,3,4,5)

def fonksiyon(isim,*args): 
    print("İsim:",isim)
    for i in args:
        print(i)
fonksiyon("Murat",1,2,3,4,5,6,7,8)


def fonksiyon(**kwargs):
    print(kwargs)
fonksiyon(isim = "Murat", soyisim = "Coşkun", numara = 12345)

#* Dikkat ederseniz 2 yıldız koyarak keyword argümanlar ile (anahtar kelimeli argümanlar) fonksiyonumuzu tanımladık ve argümanlara isim vererek fonksiyonumuzu çağırdığımızda 
#* isimleri anahtar kelime , argüman değerlerini değer olarak alarak fonksiyonumuz sözlük oluşturdu. İşte keyword argümanlar bu şekilde kullanılabiliyor.
    
def fonksiyon(**kwargs):
    for i,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)

fonksiyon(isim = "Murat", soyisim = "Coşkun", numara = 12345)


#* Şimdi de *args ve **kwargs argümanlarını beraber kullanalım.
def fonksiyon(*args,**kwargs):
    for i in args:
        print("Argümanlar:",i)
    print("------------------------------")
    for i ,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)
fonksiyon(1,2,3,4,5,6,7,isim = "Murat",soyisim = "Coşkun", numara = 12345)
        

#? İç içe fonksiyonlar
#*Pythonda fonksiyonlar da birer obje oldukları için hem bir tane değişkene atanabilirler, hem de başka bir fonksiyonun içinde tanımlanabilirler.

def selamla(isim):
    print("Selam",isim)

# Bir tane değişkene atıyoruz.
merhaba = selamla

merhaba("Ayşe") # Fonksiyon olduğu için artık bu isimle de kullanabilirim.

del selamla # Selamla fonksiyonunu siliyorum.

merhaba("Kemal") # selamla objesi silinmesine rağmen merhaba objesi silinmedi.

#* Şimdi de isterseniz iç içe fonksiyon tanımlamayı öğrenelim.

def fonksiyon():
    def fonksiyon2():
        print("Küçük fonksiyondan Merhaba")
    print("Büyük fonksiyondan Merhaba")
    fonksiyon2() # Tanımladığım fonksiyonu kullanabilirim.

fonksiyon() #Ekran çıktısı: 
#Büyük fonksiyondan Merhaba
#Küçük fonksiyondan Merhaba

fonksiyon2()  # Lokal bir değişken olduğu için fonksiyon() çağrısından sonra yok oldu. NameError hatası verir

def fonksiyon(*args): # args : (1,2,3,4,5,6)
    
    def topla(args): # (1,2,3,4,5,6)
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    print(topla(args))

fonksiyon(1,2,3,4,5,6)