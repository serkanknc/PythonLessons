
"""
Iteratorlar nedir?
Iteratorlar aslında Pythonda çoğu yerde biz görmesek de kullanılır. Iteratorlar özellikle for döngülerinde , list comprehensionlarında, ve bir sonraki derste göreceğimiz generatorlarda karşımıza çıkar.

Iteratorlar en genel anlamıyla üzerinde gezinilebilecek bir objedir ve bu obje her seferinde bir tane eleman döner.

Pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir.. Örneğin, demetlerden,listelerden ve stringlerden oluşturduğumuz bütün objeler iterable bir objedir.

Bir objenin iterable olması için hazır metodlar olan __iter()__ ve __next()__ metodlarını mutlaka tanımlaması gerekir.

"""

#? Iterator oluşturma
#* Bir iterator objesini , iterable bir objeden (liste,demet,string vs) oluşturmak için Pythonda iter() fonksiyonunu kullanıyoruz 
#* ve bu objenin bir sonraki elemanını almak için next() fonksiyonu kullanıyoruz.

liste = [1,2,3,4,5]
iterator = iter(liste) # Iterator oluşturma

next(iterator) # next metoduyla sıradaki eleman
next(iterator) # next metoduyla sıradaki eleman...

next(iterator) # Eleman kalmadığı için "StopIteration" hatası

"""
İşte iterable bir objeden bir iterator'ı bu şekilde oluşturup, next() fonksiyonuyla objenin sıradaki elemanını alabiliyoruz. 
Ancak eleman kalmayınca StopIteration hatasını alıyoruz. İşte iteratorların kullanımı bu şekildedir. 
Aslında biz farketmesek de Pythondaki for döngüleri aslında bir objenin üzerinde gezinirken iteratorları kullanır.
"""

# Aslında for döngülerinin iç yapısı şu şekildedir;

liste = [1,2,3,4,5]

iterator = iter(liste)

while True:
    try:
        print(next(iterator))
        
    except StopIteration:
        break


#? Kendi Iterable Objelerimizi Oluşturmak
#* Bunun için oluşturacağımız sınıfların mutlaka __iter()__ ve __next()__ metodlarını tanımlaması gereklidir. 
#* Şimdi bir tane kumanda sınıfı oluşturalım ve bu sınıfı iterable yapalım.
    
class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi # Kanal Listemiz
        self.index = -1 # İndeksimiz
        
    def __iter__(self):
        return self # iterator oluşturduğumuzda (iter fonksiyonu çağrıldığında )objemizi döneceğiz.
    def __next__(self): # next fonksiyonu çağrıldığında burası çalışacak.
        self.index += 1
        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration
        
kumanda = Kumanda(["Kanal d","Trt","Atv","Fox","Bloomberg"]) # Objemizi oluşturuyoruz.
iterator =  iter(kumanda) # Objemiz iterable olduğu için iterator oluşturulabilir.

next(iterator)
next(iterator)
next(iterator)#...


#* Güzel ! Objemizi iterable yapmayı başardık. Objemiz iterable olduğuna göre artık for döngüsüyle üzerinde gezinebiliriz.

for i in kumanda:
    print(i)