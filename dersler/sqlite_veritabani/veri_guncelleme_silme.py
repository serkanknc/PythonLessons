import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def veri_guncelle(yayinevi,yeni_yayinevi):

    cursor.execute("update kitaplar set Yayınevi = ? where Yayınevi = ?",(yayinevi,yeni_yayinevi))
    con.commit()
    con.close()


def veri_sil(yayinevi):
    cursor.execute("delete from kitaplar where Yayınevi = ? ",(yayinevi,))
    con.commit()
    con.close()

veri_sil("bkmkitap")

"""
Verileri Güncelleme

Tablodaki verileri güncelleme için şöyle bir sorgu kullanabiliriz.

*** Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap' -- Yayınevi 'Doğan Kitap' olan kitapların Yayınevi bilgilerini 'Everest' e günceller.***

"""

#                                       **************************************************************

"""
Verileri Silme

Tablodaki verileri silme için şöyle bir sorgu kullanabiliriz.

*** Delete From kitaplık where Yazar = 'Ahmet Ümit' -- Yazar özelliği 'Ahmet Ümit' olan kitapları tablodan siler.***

"""