import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):

        self.yazi_alani = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdır")
        self.yazi = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()

        if(sender.text() =="Temizle"):
            self.yazi_alani.clear()
        else:
            self.yazi.setText(self.yazi_alani.text())

app = QtWidgets.QApplication(sys.argv)
pencere1 = Pencere()
sys.exit(app.exec())