#Aynı List Compdaki gibi bir fonksiyonu da tek satır halinde lambda ifadeleriyle oluşturabiliriz. İlk önce yapısına bakalım sonra örneklerimize geçelim.

           #?     etiket = lambda parametre1,parametre2.... :  İşlem

# Şimdi de bu fonksiyonu lambda ifadelerini kullanarak tek satırda yazalım.

ikiyleçarp = lambda x : x * 2 # x parametre x* 2 return ifadesi ve ikiyleçarp değeri de bir etikettir(değişken gibi düşünelim

topla = lambda x,y,z : x + y + z

ters =  lambda s : s[::-1]

çifttek = lambda sayı :  sayı % 2 == 0 

#!İşte lambda ifadesini bu şekilde küçük fonksiyonlar için kullanabiliriz. 
#todo lambda ifadelerini özellikle kısa bir fonksiyonu def ifadesiyle yazmanın zahmetli olduğu zamanlarda kullanılabilir.