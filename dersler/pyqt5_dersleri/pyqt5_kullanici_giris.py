import sqlite3
import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def init_ui(self):

        self.kullanici = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş yap")
        self.yazi_alani = QtWidgets.QLabel("")
        self.uyeol=QtWidgets.QPushButton("Üye ol")
        
        self.setWindowTitle("Kullanıcı Giriş")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.uyeol)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.giris.clicked.connect(self.login)
        self.uyeol.clicked.connect(self.register)
        
        self.setLayout(h_box)
        self.show()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kullanici_giris.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "create table if not exists uyeler (kullanici_adi text, parola text)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()


    def login(self):
        k_adi = self.kullanici.text()
        parola = self.parola.text()

        sorgu = "select * from uyeler where kullanici_adi = ? and parola = ?"
        self.cursor.execute(sorgu, (k_adi, parola))
        uyeler = self.cursor.fetchall()

        if(len(uyeler)==0):
            self.yazi_alani.setText("Böyle bir kullanıcı yok.\nLütfen tekrar deneyin.")
            self.temizle()
        else:
            self.yazi_alani.setText("Hoşgeldiniz " + k_adi)
            self.temizle()

    def register(self):

        k_adi = self.kullanici.text()
        parola = self.parola.text()
        sorgu ="insert into uyeler values(?,?)"
        self.cursor.execute(sorgu,(k_adi,parola))
        self.baglanti.commit()
        self.yazi_alani.setText("Kullanıcı başarıyla eklendi.")
        self.temizle()
        
    
    def temizle(self):
        self.kullanici.clear()
        self.parola.clear()
        #self.yazi_alani.clear()
    
        
app = QtWidgets.QApplication(sys.argv)
pencere1 = Pencere()
sys.exit(app.exec())


