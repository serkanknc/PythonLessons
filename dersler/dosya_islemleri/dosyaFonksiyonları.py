
#?Dosyaları Otomatik Kapatma

# Pythonda dosyalarda işimiz bitince otomatik kapatma özelliği bulunuyor. Bundan sonra Pythonda dosya işlemlerimizi şu blok içinde yapacağız.

#                with open(dosya_adı,dosya_kipi) as file:
#                    Dosya işlemleri

with open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)

#?Dosyaları İleri Geri Sarmak

#*Ancak biz çoğu zaman dosya imlecini (file) dosyanın herhangi bir yerine götürmek isteyebiliriz. Bunun için Pythondaki seek() fonksiyonunu kullanacağız. 
#*Ancak ondan önce dosya imlecinin hangi byteda olduğunu söyleyen tell() fonksiyonuna bakalım.
        
with open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8") as file:
    print(file.tell()) #şu anda hiç işlem yapılmadığından bu kod dosyanın en başında (0. byte'da ) olduğunu gösterecektir.

with open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8") as file:
    file.seek(20) # 20.byte götürdük.
    print(file.tell()) 

with open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8") as file:
    file.seek(5) # 5.byte gidiyoruz.
    icerik = file.read(10)  # 10 karakteri okuyoruz.
    print(icerik)
    print(file.tell()) #5. byte a gittik ve 10 karakter okuduk bu yüzden en son olarak imleç 15.byte da olacaktır.


with open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8") as file:
    file.seek(5) # 5.byte gidiyoruz.
    icerik = file.read(10)  # 10 karakteri okuyoruz.
    print(icerik)
    file.seek(0)
    icerik2 = file.read(6)
    print(icerik2)
