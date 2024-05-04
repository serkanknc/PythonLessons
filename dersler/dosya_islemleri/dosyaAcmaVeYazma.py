
#?Dosya Açmak
#*Bir dosyayı açmak için open() fonksiyonunu kullanıyoruz. Yapısı şu şekildedir;

#!                open(dosya_adı,dosya_erişme_kipi)

#? "w" dosya kipi

#Dosyalarımızı açmak ve dosyalarımıza yazmak için "write" anlamına gelen "w" kipini kullanıyoruz. "w" kipi eğer oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosyayı oluşturuyor
#eğer öyle bir dosya varsa dosyayı silip tekrar oluşturuyor. Yani, eğer açmak istediğimiz dosyadan zaten varsa ve dosyanın içi doluysa "w" kipi dosyadaki bilgileri silip 
#tekrar oluşturacaktır. (Biraz Tehlikeli)"

open("bilgiler.txt","w") # Dosyayı bulunduğumuz dizinde açıyor. 

file = open("bilgiler.txt","w") # Dosya üzerinde işlem yapacak dosya imlecini file isimli değişkene atıyoruz.

#?Dosyaları Kapatmak
#*Bir dosya üzerinde işlem yaptığımızda o dosyayı kapatmak sistem kaynaklarının gereksiz kullanılmaması açısından önemlidir. 
#Çünkü programımız bitse bile dosyanın kapanacağı garanti değildir. Bu yüzden işlerimiz bittiği zaman dosyayı kapatmalıyız.

file.close()  # Dosyayı kapatmak

#*Eğer bir dosyayı bulunduğumuz dizinde değil de başka bir dizinde açmak istersek, dizinin yolunu özellikle belirtmeliyiz.

file = open("C:/Users/serkan/Desktop/bilgiler.txt","w") # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
file.close() # Unutmayalım.

#?"w" Kipiyle Dosyalara Yazmak

file = open("bilgiler.txt","w",encoding="utf-8") # Türkçe karakter kullanacaksak encoding="utf-8" parametresini veriyoruz.
file.write("Mustafa Murat Coşkun") # write fonksiyonu ile dosyamıza yazıyoruz. 20 bytelık yani 20 karakter yazıldı.
file.close()

#*Gördüğümüz gibi write fonksiyonuyla dosyamıza herhangi bir şey yazabiliyoruz. 
#*Ancak "w" kipi her seferinde dosyayı tekrar oluşturduğu için dosyayı tekrar açtığımızda bilgiler kaybolacaktır.

#?"a" Kipiyle Dosyalara Yazmak

#*"append" (ekleme) kelimesinin kısaltması olan "a" kipiyle bir dosyayı açtığımızda , dosya eğer yoksa oluşturulur. 
#Eğer öyle bir dosya mevcut ise, dosya tekrar oluşturulmaz ve dosya imleci dosyanın sonuna giderek dosyaya ekleme yapmamızı sağlar.

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Mustafa Murat Coşkun") 
file.close()

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Mehmet Gençol") # Dosyanın sonuna ekleme yaptık.
file.close()

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Mustafa Murat Coşkun\n")
file.write("Mehmet Gençol\n")
file.close()