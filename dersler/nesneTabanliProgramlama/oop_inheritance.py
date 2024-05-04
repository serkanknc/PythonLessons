"""
Peki inheritance nerede işimize yarar ? Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. 
Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor. 
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor. 
O zaman bu ortak özellikleri ve metodları tekrar tekrar bu sınıfların içinde tanımlamak yerine, 
bir tane ana class tanımlayıp bu classların bu classın özelliklerini ve metodlarını almalarını sağlayabiliriz. 
Inheritance'ın veya Kalıtım'ın temel mantığı budur.
"""

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman


class Yönetici(Çalışan): # Çalışan sınıfından miras alıyoruz.
    pass # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdir.

#* Peki biz Yönetici sınıfına ekstra fonksiyonlar ve özellikler ekleyebiliyor muyuz ? Örnek olması açısından zam_yap isimli bir metod ekleyelim.

class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı  


#?Overriding (İptal Etme)
#!Eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak , artık metodu çağırdığımız zaman miras aldığımız değil kendi metodumuz çalışacaktır. 
#*Buna Nesne Tabanlı Programlamada bir metodu override etmek denmektedir.
#todo Örneğin artık Çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfında init metodunu override edebiliriz. 
#?Böylelikle Yönetici sınıfına ekstra özellikler(attribute) ekleyebiliriz.
        
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman

class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı # Yeni eklenen özellik
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı


#super Anahtar Kelimesi
#?super anahtar kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir. 
#!Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar. Hemen örnek üzerinden anlamaya çalışalım.
        
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman

class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        super().__init__(isim,maaş,departman) # 3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz.
        
        print("Yönetici sınıfının init fonksiyonu")
        
        self.kişi_sayısı = kişi_sayısı # Ekstra özelliği de kendimiz yazıyoruz.
    def bilgilerigoster(self):
        
        print("Yönetici sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı

#* Burada super().__init() diyerek Çalışan sınıfının metodunu özel olarak çağırarak isim, maaş , departman özelliklerini bu metodla belirledik.
        
c = Yönetici("Oğuz Artıran",3000,"İnsan Kaynakları",4)
"Ekran Çıktısı aşağıda"
"Çalışan sınıfının init fonksiyonu"
"Yönetici sınıfının init fonksiyonu"