
#? Yöntem1 - import modül_adı
#! Bir modülü içeri aktarmak yani programımıza dahil etmek için import modül_adı yazabiliriz. 
#*İsterseniz bunun için math modülünü içeri aktaralım.

import math # Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.

dir(math) # Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.

help(math) # Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.


"""
#! Peki bu içeri aktarma yöntemiyle math modülünün herhangi bir fonksiyonunu nasıl kullanacağız ?

----------------------------------------------------------------------------------------------------------------------------

   #?     modül_adı.fonksiyonadı()

----------------------------------------------------------------------------------------------------------------------------

"""
math.factorial(5)
math.floor(5.4)
help(math.ceil)

#*Peki biz bir modülü kendi belirlediğimiz isimle nasıl kullanıyoruz ? Bunun için de şu şekilde bir şey yapacağız.

import math as matematik
matematik.factorial(6) # Modülü artık matematik ismiyle kullanabiliriz.

#!Yöntem2 - from modül_adı import *
#?Bir modülü programımıza dahil etmek için bu yöntemi de kullanabiliriz. İsterseniz math modülünü bu yöntem içeri aktaralım.

from math import * # Yıldızın anlamı math modülünün içindeki bütün fonksiyonları almak istediğimizi belirtiyor.

#? Böyle bir durumda math modülü içerisindeki fonksiyonları direkt olarak çağırabiliriz modül ismni kullanmamıza gerek yoktur.. 

factorial(6)
floor(4.5)

#*Peki bir modül içindeki fonksiyonların belli bir kısmını almak için ne yapacağız ? Alacağımız fonksiyonları belirtmemiz gerekiyor.

from math import factorial,floor # Sadece 2 tanesini dahil ettik.

ceil(3.4) # Dahil etmediğimiz için hata verdi.


#*Peki bu yöntemlerin birbirinden farkı ne ? 2.yöntemi kullandığımızda bildiğimiz gibi sadece fonksiyon isimlerini kullanıyoruz. 
#?Ancak eğer programa birden fazla modül dahil edersek veya dahil ettiğimiz modülün içindeki fonksiyon kendi tanımladığımız fonksiyon 
#?ismiyle aynıysa Python son gördüğü fonksiyonu çalıştıracaktır.

from math import *

def factorial(sayı):
    print("Kendi Factorial fonksiyonum.")
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        return 1
    while (sayı >= 1):
        faktoriyel *= sayı
        sayı -= 1
    return faktoriyel

factorial(5)
"Ekran Çıktısı"
#Kendi Factorial fonksiyonum.
#120


