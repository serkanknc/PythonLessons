#return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. 
#?Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir ve değeri programın başka yerlerinde kullanabiliriz. 
#Şimdi iki tane çok basit fonksiyon yazalım ve return neden gereklidir anlamaya çalışalım.

def toplama(a,b,c): # Birinci fonksiyon
    print("Toplamları",a+b+c)

def ikiyleçarp(a): # İkinci fonksiyon
    print("2 ile çarpılmış hali", a * 2)

#!Burada toplama fonksiyonundan herhangi bir değer döndürülmediği için toplam değişkenimiz hiçbir değere sahip olmadı ve tipi NoneType(atanmamış) olmuş oldu. 
#!İsterseniz burada fonksiyonları tekrardan tanımlayalım ve return mantığını anlamaya çalışalım.

def toplama(a,b,c):
    return a+b+c # return'un kullanımı 
def ikiyle_çarp(a):
    return a*2

toplam = toplama(3,4,5)
print(ikiyle_çarp(toplam))

#?İşte return ifadesinin anlamı tam olarak budur. 
#?return yardımıyla fonksiyonlar değerleri çağrıldığı yere döndürebilir ve biz de bu değerleri istediğimiz yerde kullanabiliriz.


#!return ifadesinden sonra fonksiyonumuz tamamıyla sona erer. Yani, return ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz.
def toplama(a,b,c):
    print("Toplama fonksiyonu") # Çalıştırıldı.
    return a + b + c

#todo Fonksiyonlarda çağrıldığı yere herhangi bir değer döndürmeyen(return kullanılmayan) fonksiyonlara void fonksiyonlar denmektedir. 
#todo Bunu da genel kültür olarak bilmekte fayda var.