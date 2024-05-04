
#?Dosyalarda Değişiklik Yapmak

#todo seek() ve write()
#Eğer biz bir dosyanın belli bir yerine seek() fonksiyonu ile gidip, write() fonksiyonunu kullanırsak, yazdığımız değerler öncesinde bulunan değerlerin üzerine yazılacaktır. 
#*Bunun için hem okuma hem de yazma işlemimizi yapmamızı sağlayan "r+" kipini kullanacağız.

with open("C:/Users/serkan/Desktop/deneme.txt","r+",encoding="utf-8") as file: 
    file.seek(10) # 10. byte
    file.write("Deneme") # 10.byte a gidip üzerine "Deneme" yazdı..

#? Dosyanın Sonunda Değişiklik Yapmak
    
#Dosyaların sonunda değişiklik yapmak için, dosyamızı "a" kipiyle açalım ve sadece dosyanın sonuna write() ile ekleme yapalım. bu zaten bildiğimiz bir kullanımdı.
    
with open("C:/Users/serkan/Desktop/deneme.txt","a",encoding="utf-8") as file:
    file.write("Mert Erarslan\n") # "append" metoduyla açılan bir dosyanın imleci direk dosyanın sonunda olduğu için sadece write

#?Dosyanın Başında Değişiklik Yapmak
#* "deneme.txt" dosyamızın başına bir tane satır eklemek için ne yapabiliriz? Bunun için dosyamızı bütünüyle string halinde alıp daha sonra satırımızı stringin başına eklememiz gerekiyor.
#* Daha sonra dosyanın en başına seek() fonksiyonuyla giderek ,direkt write() fonksiyonunu kullanabiliriz. Hemen yapalım."

with open("C:/Users/serkan/Desktop/deneme.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
    
    icerik = "Semih Aktaş\n" + icerik
    file.seek(0)
    file.write(icerik)

#? Dosyanın Ortasında Değişiklik Yapmak
    
#* Dosyaların ortasına herhangi bir satır eklemek için ilk olarak her bir satırı liste halinde almamızı sağlayan readlines() fonksiyonunu kullanacağız. 
#* Daha sonra bu listenin herhangi bir yerine bir eleman ekleyerek bu listeyi for döngüsü ile dosyaya yazacağız.
    
with open("C:/Users/serkan/Desktop/deneme.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Mehmet Keper\n")
    file.seek(0)
    for satır in liste:
        file.write(satır)

#todo Pythonda bir dosyaya listenin içindeki değerleri yazmak için for döngüsü dışında pratik bir fonksiyon bulunuyor. 
#todo writelines fonksiyonu içine verdiğimiz listeyi dosyaya yazacaktır.
        
with open("C:/Users/serkan/Desktop/deneme.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    file.writelines(liste)