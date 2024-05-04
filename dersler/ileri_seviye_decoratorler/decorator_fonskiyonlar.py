import time

#? Decorator Fonksiyonların Oluşturulması ve Kullanılması
#*Decorator fonksiyonlar, Pythonda fonksiyonlarımıza dinamik olarak ekstra özellik eklediğimiz fonksiyonlardır ve decorator fonksiyonların kullanımı kod tekrarı yapmamızı engeller. 
#*Pythonda decorator fonksiyonlar Flask gibi frameworklerde oldukça fazla kullanılır.


        
def kareleri_hesapla(sayılar):
    sonuç = []
    baslama =  time.time()
    
    for i in sayılar:
        sonuç.append(i ** 2)
    print("Bu fonksiyon " + str(time.time() - baslama) + " saniye sürdü.")
    
def küpleri_hesapla(sayılar):
    sonuç = []
    baslama =  time.time()
    for i in sayılar:
        sonuç.append(i ** 3)
    print("Bu fonksiyon " + str(time.time() - baslama) + " saniye sürdü.")

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
    
#* Bu iki fonksiyonda fonksiyonların çalışma sürelerini ölçmek için time modülünü kullandık. 
#* Ancak dikkat ederseniz, hem bu fonksiyonlara ekstradan iş yaptırdık , hem de 2 fonksiyonda da aynı satırları yazdık. Yani, aslında kod tekrarına düştük. 
#* Ancak eğer bu fonksiyonlara ekstra özellik ekleyen decorator bir fonksiyonumuz olsaydı, burada ne kod tekrarına düşecektik ne de fonksiyonlara ekstradan satır ekleyecektik. 
#* İşte decoratorların tam olarak önemi budur. İsterseniz zaman_hesapla isimli decorator'ımızı ilk önce yazalım

def zaman_hesapla(fonksiyon):
    def wrapper(sayılar):
        
        
        baslama = time.time()
        sonuç =  fonksiyon(sayılar)
        bitis =  time.time()
        print(fonksiyon.__name__ + " " + str(bitis-baslama) + " saniye sürdü.")
        return sonuç
    return wrapper
    
@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 2)
    return sonuç
@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 3)
    return sonuç
    

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))

#!Burada zaman_hesapla() isimli decorator bir fonksiyon yazdık. Örneğin kareleri_hesapla(range(100000)) fonksiyonu çağrılırken aslında senaryomuz şu şekilde çalışıyor;

#*        1. kareleri_hesapla fonksiyonu zaman_hesapla fonksiyonuna argüman olarak gidiyor.
#*        2. wrapper fonksiyonu kareleri_hesapla fonksiyonuna argüman olarak gönderilen 
#*        "sayılar" argümanını argüman olarak alıyor.
#*        3. wrapper fonksiyonu hem zaman hesaplama işlemini gerçekleştiriyor,hem de gönderilen
#*        fonksiyonu çalıştırıyor. Böylelikle bu fonksiyona ekstra özellik ekliyor.
#*        4.zaman_hesaplama fonksiyonu en son işlem olarak wrapper fonksiyonumuzu dönüyor.