import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazi = QTextEdit()
        self.temizle = QPushButton("Temizle")

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.temizle)

        self.setWindowTitle("QlineEdit Çalışması")
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)

        self.show()
    def click(self):
        self.yazi.clear()

app = QApplication(sys.argv)
pencere1 = Pencere()
sys.exit(app.exec())
        