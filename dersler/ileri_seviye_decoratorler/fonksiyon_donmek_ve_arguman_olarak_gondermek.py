
#? Fonksiyonları Dönmek ve Argüman Olarak Göndermek
#Bu konuda fonksiyonları return ile başka bir fonksiyondan dönmeyi ve diğer fonksiyonlara parametre olarak göndermeyi öğreneceğiz.

#? Fonksiyonları return ile Dönmek
#* Bir fonksiyon aynı zamanda bir obje olduğu için, bu fonksiyonu başka bir fonksiyondan return ile döndürebiliriz.

def fonksiyon(işlem_adı):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
        
    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım
    
    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpma
    
deneme = fonksiyon("toplama")
deneme # toplama fonksiyonuna eşit oldu.
print(deneme(1,23,23,23,2))

deneme2 = fonksiyon("çarpma")
deneme2 # çarpma fonksiyonuna eşit oldu.

#? Fonksiyonları Argüman Olarak Göndermek

def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b


def anafonksiyon(func1,func2,func3,func4,işlem_adı): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (işlem_adı == "toplama"):
        print(func1(3,4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10,3))
    elif (işlem_adı == "çarpma"):
        print(func3(10,3))
    elif (işlem_adı == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")

anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama")

anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme")

#Buradaki gibi her fonksiyonumuz aslında birer obje olduğu için diğer objeler gibi başka fonksiyonlara argüman olarak gönderilebilir. 
#Bunları da öğrendiğimize göre artık decoratorlar için hazırız.