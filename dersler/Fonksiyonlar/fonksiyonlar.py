#Python geliştiricilerin yazdığı fonksiyonlara yani bizim hazır kullandığımız fonksiyonlara(print(),type() vs.) gömülü fonksiyonlar(built-in function) denilmektedir.
#Ancak bunlardan hariç olarak biz kendi özel fonksiyonlarımızı(user-defined functions) da tanımlayabiliriz.

"""
Fonksiyonların Tanımlanması
Fonksiyon tanımlamanın yapısı şu şekildedir;

        def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
            # Fonksiyon bloğu
            Yapılacak işlemler
            # dönüş değeri - Opsiyonel

"""

def selamla(): 
    print("Selam arkadaşlar...")
    print("Nasılsınız?")

"""
Tanımlanan bir fonksiyonun kullanılmasına programlama dillerinde Fonksiyon Çağrısı denmektedir. O halde selamla fonksiyonumuzu nasıl çağıracağımızı öğrenelim. 
Fonksiyon çağrısı şu şekilde yapılabilmektedir;

        fonksiyon_adı(Argüman1,Argüman2....)
"""

selamla()
selamla("python") # Hata verdi çünkü fonksiyonumuz hiçbir değer almıyor.



#Parametreler ve Argümanlar
def selamla(isim): # isim değişkenimiz burada parametre olmaktadır
    print("Merhaba:",isim)
selamla("Kemal") # "Kemal" değeri burada  argüman olmaktadır. 

#! "NOT: Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre , fonksiyon çağrısı yaptığımız zaman içine gönderdiğimiz değerler ise Argüman olmaktadır."

# Toplama fonksiyonu
def toplama(a,b,c):
    print("Toplamları:",a+b+c)

toplama(3,4,5)


def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)
