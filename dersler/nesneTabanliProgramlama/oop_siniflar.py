"""

 Class Anahtar Kelimesi

Sınıflar veya Classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını tanımladığımız bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz. 
İsterseniz bir Araba classı tanımlayarak yapımızı kurmaya başlayalım.


"""

#  Yeni bir Araba veri tipi oluşturuyoruz.
class Araba():
    model =  "Renault Megane"
    renk = "Gümüş"            # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4

#todo Sınıfımızı Pythonda tanımladık. Peki bu sınıftan obje nasıl oluşturacağız ? Bunu da şu şekilde yapabiliyoruz.

#*----------------------------------------------------------------------------------------------------------------------------

    #? obje_ismi = Sınıf_İsmi(parametreler(opsiyonel))
     
#*----------------------------------------------------------------------------------------------------------------------------
    
araba1 =  Araba() # Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.
type(araba1)

#? araba1 objesi artık sınıfta tanımladığımız bütün özelliklere (attributes) sahip olmuş oldu. 
#todo İşte sınıf ve obje üretmek bu şekilde olmaktadır. Peki bu araba objesinin özelliklerinin nasıl görebiliriz ?

#*--------------------------------------------------------------------------------------------------------------------------

       #? obje_ismi.özellik_ismi
#*--------------------------------------------------------------------------------------------------------------------------
araba1.model
araba1.renk


#?Burda gördüğümüz gibi oluşturduğumuz objelerin buradaki model,renk vs. gibi özelliklerinin değeri aynıdır. 
#todo Çünkü aslında burada tanımladığımız özellikler birer sınıf özelliğidir. 
#!Yani biz bir obje oluşturduğumuzda bu özelliklerin değerleri varsayılan olarak gelir. Bu özelliklerin değerlerine , herhangi bir obje oluşturmadan da erişebiliriz.
#*Bunu da şu şekilde yapabiliriz.

Araba.renk # Class_İsmi.özellik_ismi


#?Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamız için her bir objeyi oluştururken objelerin değerlerini göndermemiz gerekiyor. 
#*Bunun için de özel bir metodu kullanmamız gerekmektedir __init()__ 

#! Aslında init metodu Pythonda yapıcı(constructor ) fonksiyon olarak tanımlanmaktadır. Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur. 
#*Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle oluşturabiliriz.

#? Araba Veri tipi 

class Araba():
    # Şimdilik Class özelliklerine ihtiyacımız yok.
    
    def __init__(self):
        print("init fonksiyonu çağrıldı.")

#!self anahtar kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren bir referanstır ve metodlarımızda en başta bulunması gereken bir parametredir. 
#Yani biz bir objenin bütün özelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.
        
#? Objeler oluşturulurken, Python bu referansı metodlara otomatik olarak kendisi gönderir. Özel olarak self referansını göndermemize gerek yoktur.
class Araba():
    
    def __init__(self,model,renk,beygir_gücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model =  model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk = renk # self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygir_gücü = beygir_gücü # self.özellik_ismi = parametre değeri şeklinde objemizin beygir_gücü özelliğine değeri atıyoruz.
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özelliğine değeri atıyoruz.

# araba1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.
araba1 = Araba("Peugeot 301","Beyaz",90,4) 

#? İstersek init metodunu varsayılan değerlerle de yazabiliriz.

class Araba():
    
    def __init__(self , model = "Bilgi Yok",renk = "Bilgi Yok",beygir_gücü = 75 ,silindir = 4): 
        self.model =  model 
        self.renk = renk 
        self.beygir_gücü = beygir_gücü 
        self.silindir = silindir

araba1 = Araba(beygir_gücü = 85, renk = "Siyah")

#*İşte burada gördüğümüz gibi bir objeyi init metodunu kendimiz yazarak farklı değerlerle oluşturabiliyoruz.