import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def veri_listele():
    cursor.execute("select * from kitaplar")
    data = cursor.fetchall()

    print("Bilgiler getiriliyor...")
    for i in data:
        print(i)
    con.close()

def veri_listele2(yayinevi):
    cursor.execute("select * from kitaplar where Yayınevi = ? ",(yayinevi,))
    data = cursor.fetchall()

    print("Bilgiler getiriliyor...")
    for i in data:
        print(i)
    con.close()

veri_listele()

"""
Tablodaki Verileri Çekme

Önceki derslerimizde Tablo oluşturmayı ve Tabloya veri eklemeyi öğrenmiştik. Bu derste de tablodaki verileri nasıl çekeceğimizi öğrenmeye çalışacağız. 
Tablodan veri çekmek için şu SQL sorgularını kullanacağız.

Select * From kitaplık  -   Tablodaki tüm bilgileri almamızı sağlar.

Select İsim,Yazar From kitaplık  -   Tablodaki tüm bilgileri sadece İsim ve Yazar özelliklerini almamızı sağlar.

Select * From kitaplık where Yayınevi = 'Everest'  -  Sadece Yayınevi özelliği Everest olanları alır.

"""