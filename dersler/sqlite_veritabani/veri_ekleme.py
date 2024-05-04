import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()


def deger_ekle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("insert into kitaplar values (?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
    con.close()

isim= input("İsim: ")
yazar= input("Yazar: ")
yayinevi= input("Yayınevi: ")
sayfasayisi= int(input("Sayfa: "))

deger_ekle(isim,yazar,yayinevi,sayfasayisi)


"""
Tablolara Veri Ekleme

insert into tablo_adi values (deger1,deger2,deger3,....)

"""