"""while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder. 
while döngülerinin sona ermesi için koşul durumunun bir süre sonra False olması gereklidir.Yapısı şu şekildedir;

                            while (koşul):
                                İşlem1
                                İşlem2
                                İşlem3
                                  //
                                  //

"""
# Döngüde i değerlerini ekrana yazdırma

i = 0 

while (i < 10):
    print("i'nin değeri",i)
    i += 1 # Koşulun bir süre sonra False olması için gerekli - Unutmayalım

    # Ekrana 40 defa "Python Öğreniyorum" yazdıralım.
i = 0

while (i < 40):
    print("Python Öğreniyorum")
    i +=1

    # Liste üzerinde indeks ile gezinme
liste = [1,2,3,4,5]

a = 0 

while (a < len(liste)):
    print("Indeks:",a,"Eleman:",liste[a])
    a +=1


    # Bu kodu çaıştırmayalım. Jupyter sıkıntı çıkarabilir :)
i = 0 
while (i < 10):
    print(i)
    # i değişkenini artırma işlemi yapmadığımız için i değişkeninin değeri sürekli 0 kalıyor 
    # ve döngü koşulu sürekli True kalıyor.