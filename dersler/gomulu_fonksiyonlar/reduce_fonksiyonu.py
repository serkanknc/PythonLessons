from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.


#? Pythonda gömülü bir fonksiyon olan reduce() fonksiyonunun yapısı şu şekildedir.

#*                  reduce(function, iterasyon yapılabilen veritipi(liste vb.))
            
            
#reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve daha sonra çıkan sonucu listenin 3. elemanına uygular 
#ve bu şekilde devam ederek liste bitince bir tane değer döner.

reduce(lambda x,y : x + y , [12,18,20,10])

# Bakın 5'in faktöriyelini bulduk.
reduce(lambda x,y : x * y , [1,2,3,4,5])

reduce(lambda x,y : x * y , [3,4,5,10])

# max fonksiyonu()
max([1,2,3,4,5,6])

# reduce ile max fonksiyonu
def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

print(reduce(maksimum, [-2,1,100,35,32]))

