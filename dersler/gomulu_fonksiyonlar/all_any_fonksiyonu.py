

#* all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
liste = [True,False,True,False,True]
print(f"değer = {all(liste)}")

liste1 = [1,2,3,4,5]
print(f"değer = {all(liste1)}")



#* any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
liste3 = [True,False,True,False,True]
print(f"değer = {any(liste3)}")

liste4 = [0,0,0,0,0,0,0]
print(f"değer = {any(liste4)}")