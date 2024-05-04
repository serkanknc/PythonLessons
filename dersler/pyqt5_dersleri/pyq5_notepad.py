import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.dosya_ac = QPushButton("Dosya Aç")
        self.dosya_kaydet = QPushButton("Dosya Kaydet")

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.dosya_ac)
        h_box.addWidget(self.dosya_kaydet)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.temizle_fonksiyon)
        self.dosya_ac.clicked.connect(self.ac_fonksiyon)
        self.dosya_kaydet.clicked.connect(self.kaydet_fonksiyon) 
        self.show()
    def temizle_fonksiyon(self):
        self.yazi_alani.clear()
    def ac_fonksiyon(self):
        dosya_isim = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_isim[0],"r",encoding="utf-8") as file:
            self.yazi_alani.setText(file.read())
    def kaydet_fonksiyon(self):
        dosya_isim = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

        with open (dosya_isim[0],"w",encoding="utf-8") as file:
            file.write(self.yazi_alani.toPlainText())
    
app = QApplication(sys.argv)
pencere1 = Pencere()
sys.exit(app.exec())