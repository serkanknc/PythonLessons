#\n karakteri Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa alt satırdan ekrana yazdırma işlemine devam eder.
print("Merhaba\nNasılsın\nİyi misin")

#t karakteri Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa bir tab boşluk bırakarak ekrana yazdırma işlemine devam eder.
print("Ocak\tMart\tŞubat")

#type () fonksiyonu içine gönderilen değerin hangi veri tipinden olduğunu söyler.
a = 65
print(type(a))

#print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız değerlerin arasına istediğimiz karakterlerin yerleştirilmesini sağlar. 
#Eğer bu parametreyi kullanmazsak değerlerin arasına varsayılan olarak boşluk yerleştirilir

print(3,4,5,6,7,8,9)
print(3,4,5,6,7,8,9,sep = ".")
print("06","04","2015",sep = "/")

#Eğer bir stringin başına * işareti koyup, print fonksiyonuna gönderirsek bu string karakterlerine ayrılacak
#ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacaktır.

print(*"Merhabalar")
print(*"Python",sep = "\n")

#Programlama yaparken bazı yerlerde bir stringin içinde daha önceden tanımlı string,float, int vs. değerleri yerleştirmek isteyebiliriz. 
#Böyle durumlar için Pythonda format() fonksiyonu bulunmaktadır.

print("{} {} {}".format(3.1423,5.324,7.324324))

a = 3
b = 4
print("{} + {} 'nin toplamı {}'dır".format(a,b,a+b))


#Süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.
print("{1} {0} {2}".format(43,"Murat",54))

# Süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimiz söylüyor

print("{:.2f} {:.2f} {:.3f}".format(3.1463,5.324,7.324324))