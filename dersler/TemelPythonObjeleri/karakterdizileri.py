karakter = "python programlama ve kodlama"

karakter1 = "python programlama ve kodlamaaaaaaa"

karakter2 = "python programlamaaaaaaaaa ve kodlama"

print(karakter)

# len() fonksiyonu stringin uzunluğunu bulur.
print(len(karakter))

#string indeksleme ve parçalama. indeksler sıfırdan başlar ve indeks numaraları ile string içindeki karakterlere erişebiliriz.
print(karakter[0])
print(karakter[6])
print(karakter[15])


#stringlerin belirli kısmını elde etme
print(karakter[4:10])
print(karakter[4:20:2])
print(karakter[:20])
print(karakter[4:])
print(karakter[:])
print(karakter[:-5])
print(karakter[::-1])

karakter = karakter +" merhabalar"
print(karakter)

# string toplama birleştirme
print(karakter + " pytho ekstasdsss")

print(karakter+" "+karakter1+" "+karakter2)

print(karakter1* 3)



