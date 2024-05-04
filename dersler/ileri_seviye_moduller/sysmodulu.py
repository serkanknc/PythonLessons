import sys

#? sys Modülü
#* sys modülü bizim sistemimizde kurulu olan Python sürümünü yönettiğimiz standard bir modüldür.Bu modülü kullanarak Python sistemine özgü fonksiyonları ve özellikleri kullanabiliriz. 

#? sys.exit() fonksiyonu
#* Bu fonksiyon çalışan Python programımızı sonlandırır.

a = input("a:")
b = input("b:")

sys.exit()

c = input("c:")



#? stderr ve stdout
#* Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.


"""
stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.

stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.

stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.
"""

#* Biz print() fonksiyonumuzu kullandığımızda aslında standard olarak stdout kullanılmaktadır. Ancak biz istersek ***stderr'e de ** bir şeyler yazabiliriz.

sys.stderr.write("Burası bir hata mesajı\n")

sys.stderr.flush() # Buffer'ı hemen yaz. 

sys.stdout.write("Burası normal çıktımız\n")

#? sys.argv
#* sys.argv Python programlarını komut satırlarından çalıştırdığımızda yanına verdiğimiz argümanları taşıyan bir listedir.

def kok_bulma(a,b,c):
    delta = b**2 -4 *a*c

    if(delta < 0 ):
        print("Reel kök yok")
    else:
        x1 = (-b -delta ** 0.5) / (2*a)
        x2 = (-b +delta ** 0.5) / (2*a)
        return(x1,x2)

if(len(sys.argv)== 4):

    print("Kök bulma", kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerleri giriniz.")
    sys.stderr.flush()