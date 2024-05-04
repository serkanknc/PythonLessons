import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (isim text, yazar text, yayinevi text, sayfa_sayisi int)")
    con.commit()
    con.close()

tablo_olustur()


"""
Sqlite Veritabanı Oluşturma
            1. import sqlite3 -  Modülümüzü dahil ediyoruz.
            2. con = sqlite3.connect("kütüphane.db") - kütüphane.db veritabanını oluşturup bağlanıyoruz.
            Eğer öyle bir veritabanı varsa bağlanıyoruz. Bağlantıyı con isimli bir değişkene atıyoruz.
            3.  Database üzerinde Sql sorgularını çalıştırmak için cursor bir tane imleç oluşturuyoruz. 
            "cursor =  con.cursor()
            4. Veritabanı işlemlerinin sonunda con.close() ile bağlantımızı koparıyoruz.

"""

"""
Kitaplık Tablosu oluşturma


Veritabanında kitaplık isimli bir tablo oluşturmak için şu 2 sorgudan birini kullanabiliriz.

*** CREATE TABLE kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) 
Bu sorgu kitaplık isimli bir tablo oluşturacak ve bu tablonun özellikleri İsim (TEXT --> String),Yazar(TEXT --> String),Yayınevi (TEXT ---> String), Sayfa_Sayısı(INT --- int) olacak. 
Ancak bu sorguyu arda arda çalıştırırsak "Tablo Already Exists" hatası alacağız.

*** CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) 
Bu sorgu tablo yoksa oluşturacak, tablo varsa hata vermeyecektir. 

"""