
#? Bu konuda filter fonksiyonunu öğrenmeye çalışacağız.

#                filter(fonksiyon,iterasyon yapılabilen bir veritipi(liste vb.))


#* filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır ve liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular. 
#*filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner.

list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])) # Çift olan sayılar

def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True


list(filter(asal_mi,range(1,100))) # 1 den 100' e kadar olan asal sayılar.

#örnek
def cift_sayilar_filtrele(liste):
    return list(filter(lambda x: x % 2 == 0, liste))

# Bir liste tanımla
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Çift sayıları filtrele
cift_sayilar = cift_sayilar_filtrele(sayilar)

# Sonucu ekrana yazdır

print(f"Cift Sayılar:  {cift_sayilar}")