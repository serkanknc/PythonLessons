
#?Dosya Okuma İşlemleri
#*Dosyaları okumak ve verileri almak için "r" kipiyle açmamız gerekiyor. "r" kipiyle açtığımız dosya eğer bulunmuyorsa "FileNotFoundError" hatası dönecektir. 
#*Şimdi bulunduğumuz dizinde bulunan "bilgiler.txt" dosyasını açalım.

file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8")
file.close()

file = open("bilgiler2.txt","r",encoding="utf-8")  # böyle bir dosya yok . O yüzden FileNotFoundError hatası döndü.


#todo Dosya işlemlerini daha güvenli yazmak try,except bloklarını kullanabilirsiniz

try:
    file = open("bilgiler2.txt","r",encoding= "utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı....")# böyle bir dosya olmadığından except bloğu çalışacak..


#?For döngüsü ile okuma
file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8") # Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.

for i in file: # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i) # Her bir satırı ekrana basıyoruz.
file.close()   
#! Ekran çıktısında her bir satır bir tane boşluklu yazılıyor.. bunun sebebi dosyaya yazarken her satır sonunda \n karakteri olması ve print fonksiyonunun 
#! bir alt satıra geçmek için boşluk bırakması. 
#* Bunu önlemek için varsayılan değer olarak "\n" karakteri alan end parametresine kendimiz değer verebiliriz.

file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8")  # Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.

for i in file: # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i,end = "") # Her bir satırı ekrana basıyoruz. end parametresi \n yerine boşluk alacak.
file.close()

#?read() fonksiyonu

#*read() fonksiyonu eğer içine hiçbir değer vermezsek bütün dosyamızı okuyacaktır.
file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8")
icerik = file.read() 
print("Dosya İçeriği:\n",icerik,sep ="")
file.close()

#read() fonksiyonuyla bir dosyayı okuduğumuzda dosya imlecimiz dosyanın en sonuna gider ve read() fonksiyonu 2. okuma da artık boş string döner.
file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8")
icerik = file.read() 
print("1. Okuma : Dosya İçeriği:\n",icerik,sep ="")

icerik2 = file.read()
print("2. Okuma : Dosya İçeriği:\n",icerik2,sep ="")
file.close()

#?readline() fonksiyonu

#readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde dosya imlecimiz (file) bir satır atlayarak devam eder.
file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline()) # Okuyacak herhangi bir şey kalmayınca readline fonksiyonu boş string döner.
file.close()

#?readlines() fonksiyonu

#readlines() fonksiyonu dosyanın bütün satırları bir liste şeklinde döner.
file = open("C:/Users/serkan/Desktop/deneme.txt","r",encoding="utf-8")
liste =file.readlines()
print(liste)
file.close()