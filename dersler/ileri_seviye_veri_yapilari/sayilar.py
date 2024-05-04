
#? Şimdi isterseniz 10'luk tabandaki bir sayıyı ikilik tabana çevirmek için kullanılan bin() fonksiyonuna bakalım.

bin(4) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)

#? Şimdi de 10'luk tabandaki bir sayıyı 16'lık tabana çevirmek için kullanılan hex() fonksiyonuna bakalım.

hex(32) # Sayımız 16'lık tabanda yazıldı.

#! Fonksiyonlar
#?abs fonksiyonu Sayının mutlak değerini almamızı sağlar.

abs(-4)
abs(-5)

#? round fonksiyonu Sayıları alta veya üste yuvarlar.

round(3.7)

#? max ve min fonksiyonu

#* max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.
#* min() fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür.

max(3,4) # İstediğimiz kadar değer verebiliriz.
max([13.2,-4.32,1.2,15.6]) # Sayıları liste şeklinde de verebiliriz.
max((13.2,-4.32,1.2,15.6)) # Sayıları demet şeklinde de verebiliriz.

min([13.2,-4.32,1.2,15.6])
min(3,4)
min((13.2,-4.32,1.2,15.6))


#? sum fonksiyonu

#*sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.

sum(3,4) #! hatalı kullanım...

sum([3,4,5,6,7])
sum((3,4))

#? pow fonksiyonu

#* pow() fonksiyonu üs alma işlemlerinde kullanılır.

pow(2,4) # 2 üzeri 4
pow(3,4) # 3 üzeri 4