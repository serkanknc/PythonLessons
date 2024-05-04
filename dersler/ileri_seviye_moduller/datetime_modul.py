from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"tr_TR")

#? DateTime Modülü
#DateTime modülü Pythonda zaman ve tarih işlemleri için kullandığımız hazır bir modüldür.

#?Şu anki zamanı alma - now()

su_an = datetime.now()
print(su_an)
print(su_an.year)
print(su_an.month)
print(su_an.hour)

#? ctime() fonksiyonu
#* Şu anki zamanı daha güzel göstermek için ctime() fonksiyonunu kullanabiliriz.

print(datetime.ctime(su_an))

#? strftime() fonksiyonu
#* şu anki zamanın yıl, ay , gün gibi özelliklerin sadece belli bir kısmını göstermek için kullanılır

"""
Yıl bilgisini almak için : %Y
    
Ay ismini almak için : %B

Gün ismini almak için : %A

Saat bilgisini almak için : %X

Gün bilgisini almak için : %D
"""

print(datetime.strftime(su_an,"%Y"))
print(datetime.strftime(su_an,"%B"))
print(datetime.strftime(su_an,"%A"))
print(datetime.strftime(su_an,"%X"))
print(datetime.strftime(su_an,"%D"))
print(datetime.strftime(su_an,"%Y %B %A"))



#? timestamp() ve fromtimestamp()
#* Şu anki zamanı saniye cinsinden bulmak için, datetime objemizi (şu_an objesi) timestamp() fonksiyonumuza gönderebiliriz. 
#* Aynı zamanda saniye cinsinden verilmiş bir zamanı da fromtimestamp fonksiyonuyla datetime objesine çevirebiliriz.


saniye = datetime.timestamp(su_an)
zaman = datetime.fromtimestamp(saniye)

print(saniye)
print(zaman)

#todo fromtimestamp() fonksiyonun içine 0 değerini verirsek 1970-01-01 03:00:00 değeri döndürür. çünkü bilgisayar zaman sayacı 1970 tarihinde başlamıştır. 
#todo bilgisayarlar o tarihten itibaren sürekli saniye sayarlar.

#? Belli iki tarih arasındaki farkı bulmak

tarih = datetime(2020,5,6)

suan= datetime.now()

fark = suan-tarih
print("iki tarihin farkı ",fark)
print(fark.days)
print(fark.seconds)
print(fark.microseconds)