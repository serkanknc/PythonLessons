

"""
Generatorlar Pythonda iterable objeler (örnek olarak fonksiyonlar) oluşturmak için kullanılan objelerdir ve bellekte herhangi bir yer kaplamazlar. 
Örneğin, 100.000 tane değer üretip, bu değerleri bir listede tutmak bellekte oldukça fazla yer kaplayacaktır. 
O yüzden bu işlemi gerçekleştiren bir fonksiyonu generator fonksiyon şeklinde yazmak oldukça mantıklı olacaktır. 
Generatorları anlamak için isterseniz bir fonksiyonu ilk olarak generator kullanmadan yazmaya çalışalım.
"""

#? Generatorların Oluşturulması ve Kullanılması

def karelerial():
    for i in range(1,6):
        yield i ** 2 # yield anahtar kelimesi generator'un değer üretmesi için kullanılıyor.
generator =  karelerial()

print(generator) # Generator objesi

"""
Generatorle yazdığımız fonksiyonda yield anahtar kelimesiyle değerleri ürettiğimizi sanıyoruz. 
Ama aslında bu fonksiyonu çağırınca bize sadece bir tane generator objesi dönüyor ve biz sadece generator objesinin değerlerine ulaşmaya çalıştığımızda değerler tek tek üretiliyor. 
Yani kısacası bellekte değerler tutulmuyor. Bu generator objesinin üzerinde bir tane iterator oluşturarak durumu daha iyi anlamaya çalışalım.
"""
iterator = iter(generator)

print(next(iterator)) # 1 değeri üretildi
print(next(iterator)) # 4 değeri üretildi 1 değeri tarihe karıştı.
print(next(iterator)) # 9 değeri üretildi 4 değeri tarihe karıştı.
print(next(iterator)) # 16 değeri üretildi 9 değeri tarihe karıştı
print(next(iterator)) # 25 değeri üretildi 16 değeri tarihe karıştı.
print(next(iterator)) # Üretilecek değer kalmadı.

"""
Aslında generator objesi sadece değerlere ulaşmak istediğimiz zaman yield anahtar kelimesini kullanıp değer üretiyor. 
Yani generatorler sadece biz değerlere ulaşmak istersek çalışıyor. İşte generatorlerin mantığı tamamıyla bu şekilde ! 
Şimdi de list comprehensionları generatorlara çevirmeye çalışalım.
"""

liste = [i * 3 for i in range(5)]
#* Böyle bir list comprehension'ı generator objesine çevirmek için [] yerine () kullanıyoruz.

generator = (i * 3 for i in range(5))

iterator = iter(generator)
print(next(iterator))
print(next(iterator))#...


#örnek 
def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield f"{i} x {j} = {i*j}"

for i in carpimtablosu():
    print(i)

# Buradaki bu kadar işlemi listelerde tutmak o kadar mantıklı değil. 
# Onun yerine bellekte yer kaplamayan ve sadece her ulaşmaya çalıştığımızda değer üreten(yield) generator fonksiyonları kullanmak daha mantıklı olacaktır.
    
#todo Peki generatorlar Pythonda nerede kullanılıyor ? Aslında bizim daha önce öğrendiğimiz range fonksiyonu Pythonda generatorlar yazılmış bir fonksiyondur.
    
for i in range(100): # Sadece istediğimiz zaman sayılara ulaşıyoruz.
    print(i)