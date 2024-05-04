
#? Demet elemanları parantez içine alınarak demet oluşturulabilir.
demet = (1,2,3,4,5,6,7,8,9)

# type() fonksiyonu yardımıyla türünü öğrenelim.
type(demet)

# Tek elemanlı demet bu şekilde tanımlanabilir.
demet = (1,)

demet = (1,2,3,4,5,6,7)
# 0. indekse  ulaşma
demet[0]

# Demeti oluşturalım.
demet = (1,2,3,"Mustafa","Murat","Coşkun")
# "Mustafa" elemanının indeksini buluyoruz.
demet.index("Mustafa")

#count metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.
demet = (1,23,34,34,2,1,4,5,1,1,34)
demet.count(1)

