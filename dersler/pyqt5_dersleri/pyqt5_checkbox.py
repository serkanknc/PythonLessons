import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.checkbox = QCheckBox("Python'u seviyorsanız seçim yapın!")
        self.yazi_alani =QLabel("")
        self.buton = QPushButton("Tıklayın")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Checkbox Seçimi")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))

        self.show()

    def click(self,checkbox,yazi_alani):
        if(checkbox):
            yazi_alani.setText("Pythonu seviyorsunuz..")
        else:
            yazi_alani.setText("Pythonu sevmiyorsunuz !")

app = QApplication(sys.argv)
pencere1 = Pencere()
sys.exit(app.exec())