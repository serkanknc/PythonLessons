#Pythondaki bu hazır fonksiyon bizim verdiğimiz değerlere göre range isimli bir yapı oluşturur ve bu yapı listelere oldukça benzer. 
#Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak listelere benzeyen bir sayı dizisi oluşturur. Kullanımlarını öğrenmeye başlayalım.

print(*range(0,20)) # Yazdırmak için başına "*" koymamız gerekiyor.

liste = list(range(0,20)) # list fonksiyonuyla listeye dönüştürebilir.

print(*range(15)) # Başlangıç değeri vermediğimiz 0'dan başlar 

print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.

print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.

for sayı in range(0,10):
    print(sayı)

for sayı in range(1,20):
    print("* " * sayı)
