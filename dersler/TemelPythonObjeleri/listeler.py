# liste değişkeni. Değişik veri tiplerinden değerleri saklayabiliyoruz.
liste =  [3,4,5,6,"Elma",3.14,5.324]
liste

# Boş liste
bos_liste = []
print(bos_liste)

# Boş liste . list() fonksiyonuyla da oluşturulabilir.
bos_liste = list()
print(bos_liste)

# len fonksiyonu listeler üzerinde de kullanılabilir.
liste3 = [3,4,5,6,6,7,8,9,0,0,0]
print(len(liste3))


liste = [1,2,3,4,5]
liste * 3
print(liste)

#Bir string list() fonksiyonu yardımıyla listeye dönüştürülebilir.

s =  "Merhaba"
lst =  list(s)
print(lst)

#Listeleri indeksleme ve parçalama stringlerle birebir olarak aynıdır.
liste = [3,4,5,6,7,8,9,10]
print(liste)    

# 0. eleman 
liste[0]

# Sonuncu Eleman
liste[len(liste)-1]

# Sonuncu Eleman
liste[-1]

# İlk Eleman
liste[-len(liste)]

#Bir listeyi birbirine toplama işlemini stringlerdeki gibi yapabiliriz.

liste1 =  [1,2,3,4,5]
liste2 =  [6,7,8,9,10]
liste1 + liste2

#append metodu, verdiğimiz değeri listeye eklememizi sağlar.
liste = [3,4,5,6]
liste.append(7)
liste

#Bu metod, içine değer vermezsek listenin son indeksindeki elemanı, 
#değer verirsek verdiğimiz değere karşılık gelen indeksteki elemanı listeden atar ve attığı elemanı ekrana basar.
liste = [1,2,3,4,5]
liste.pop()

liste = [34,1,56,334,23,2,3,19]
liste.sort() # Küçükten büyüğe sıralar.
liste

liste.sort(reverse = True) # Büyükten küçüğe sıralar.
liste

liste = ["Elma","Armut","Muz","Kiraz"]
liste.sort() # Alfabetic olarak küçükten büyüğe
liste

# 3 Tane liste oluşturalım.

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]

yeniliste = [liste1,liste2,liste3]
yeniliste

# 1.elemanın 0.elemanı
print(yeniliste[1][0])# 4 sayısını ekrana basar