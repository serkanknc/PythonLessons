"""
Özel metodlar, daha önceden de bahsettiğimiz gibi bizim özel olarak çağırmadığımız ancak her classa ait metodlardır. 
Bunların çoğu biz tanımlamasak bile Python tarafından varsayılan olarak tanımlanır. Ancak bu metodların bazılarını da özel olarak bizim tanımlamamız gerekmektedir.
"""

class Kitap():
    pass

kitap1 = Kitap() # __init__ metodu çağrılıyor.

len(kitap1) # __len__ metodu çağrılacak ancak tanımlı değil. Bunu özellikle bizim tanımlamamız gerekiyor.
"HATA MESAJI"

print(kitap1) # __str__ metodu çağrılır.
"EKRAN ÇIKTISI"
"<__main__.Kitap object at 0x000000CEE4E93390>"


del kitap1 # del anahtar kelimesi bir objeyi siler ve __del__ metodu çağrılır. 

#?init metodu
#*init metodunu kendimiz tanımlarsak artık kendi init fonksiyonumuz çalışacaktır.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür

#?str metodu
#TODO Normalde print(kitap1) ifadesi ekrana şöyle bir yazı yazdırıyor. str metodunu kullanırken return ifadesini kullanmamız gerekli
"<__main__.Kitap object at 0x000000CEE886EAC8>"

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    
#!len metodu
#*len metodu normalde özel olarak biz tanımlamazsak tanımlanan bir metod değil. Onun için bu metodu kendimiz tanımlamamız gereklidir.
    
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    

kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
len(kitap1) # KEndi __len__ metodumuz çağrıldı.
"ekran çıktısı: 561"

#?del metodu
#*del metodu Pythonda bir objeyi del anahtar kelimesiyle sildiğimiz zaman çalıştırılan metoddur. Bu metodu kendimiz tanımlayarak ekstra özellikler ekleyebiliriz.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.......")