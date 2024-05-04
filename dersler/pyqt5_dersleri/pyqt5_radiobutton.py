import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.radio_yazi = QLabel("Hangi dili seçmek istiyorsunuz ?")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.ccharp = QRadioButton("C#")
        self.radio_result = QLabel("")
        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_yazi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.ccharp)
        v_box.addStretch()
        v_box.addWidget(self.radio_result)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Radio Seçme")

        self.buton.clicked.connect(lambda: self.click(self.python.isChecked(),self.java.isChecked(),self.ccharp.isChecked(),self.radio_result))
        self.show()

    def click(self,python,java,ccharp,yazi_alani):
        if(python):
            yazi_alani.setText("Python")
        if(java):
            yazi_alani.setText("Java")
        if(ccharp):
            yazi_alani.setText("C#")


            

app = QApplication(sys.argv)
pencer1 = Pencere()
sys.exit(app.exec())