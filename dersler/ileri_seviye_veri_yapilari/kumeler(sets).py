
#? Kümeler(Sets)
#* Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veritipidir. Bu açıdan kullanıldıkları yerlerde çok önemli bir veritipi olmaktadırlar.

#? Küme oluşturmak

x =  set() # Boş küme

liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste) # Veri tipi dönüşümü
print(x)# Aynı elemanlar tek bir elemana indirgendi.

x = set("Python Programlama Dili")  # Aynı karakterler tek bir karaktere indirgendi.

x = {"Python","Php","Python"}
print(x) # Aynı elemanlar teke indirgendi.

#? For döngüsüyle Gezinmek
#* Kümeler de tıpkı sözlükler gibi sırasız bir veri tipidir. Bunu for döngüsüyle görebiliriz.

x = {"Python","Php","Java","C","Javascript"}

for i in x:
    print(i) 

#! Bir kümenin elemanlarına direkt olarak ulaşamayız bu işlemler kümelerde tanımlı değildir.. ne indexle ne de eleman ismiyle 
#? Erişmek için mutlaka veri tipi dönüşümü yapmalıyız...
    
liste = list(x)

print(liste[0])

#? Kümelerin Metodları
#* Eleman Eklemek : add() metodu
#* kümeye eleman eklemimizi sağlar. Aynı eleman eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz.
    
x = {1,2,3}
x.add(4)

#? İki kümenin farkı : difference() metodu
#* Bu metod birinci kümenin ikinci kümeden farkını döner.
#todo            küme1.difference(küme2) # Küme1'in Küme2'den farkı

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.difference(küme2)

#? İki kümenin farkı ve güncelleme : difference_update() metodu
#* Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.
#todo            küme1.difference_update(küme2) # Küme1'in Küme2'den farkı

küme1.difference_update(küme2)

#? Kümeden Eleman Çıkartmak : discard() metodu
#* İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).

küme1.discard(2)

#? Küme kesişimleri : intersection() metodu
#* Bu metod iki kümenin kesişimleri bulmamızı sağlar.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.intersection(küme2)

#? Küme kesişimleri ve güncelleme : intersection_update() metodu
#* Bu metod birinci kümeyle ikinci kümenin kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.intersection_update(küme2)

#? Kümeler ayrık küme mi ? : isdisjoint() metodu
#* Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}

küme1.isdisjoint(küme2)#false
küme1.isdisjoint(küme3)#true


#? Alt kümesi mi ? : issubset() metodu
#* Bu metod , birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.

küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme3 = {5,6,7}

küme1.issubset(küme2)#true
küme1.issubset(küme3)#false

#? Birleşim Kümesi : union() metodu
#* Bu metod, iki kümenin birleşim kümesini döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.union(küme2)

#? Birleşim Kümesi ve update : update() metodu
#* Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.update(küme2)