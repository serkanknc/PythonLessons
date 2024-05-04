import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv) #Uygulama oluşturmak istiyoruz

    pencere = QtWidgets.QWidget() #bu fonksiyon ile pencere oluşutrduk
    pencere.setWindowTitle("PyQt5 Uygulaması")# pencereye bir başlık verdik
    pencere.setGeometry(500,200,1024,768)
    tamam = QtWidgets.QPushButton("Tamam")
    iptal = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()#hbox oluşturuldu
    
    h_box.addWidget(tamam)#içine widget olarak buton eklendi
    h_box.addStretch()#kullanıma göre sağa ya da sola butonları yaslar
    h_box.addWidget(iptal)
    
    v_box = QtWidgets.QVBoxLayout()
    
    v_box.addLayout(h_box)
    
    
    
    pencere.setLayout(v_box)#pencerenin içine layout set ettik yerleştirdik


    """
    buton = QtWidgets.QPushButton(pencere)#Butonu oluşturduk ve pencerenin içine yerleştirdik
    buton.setText("BUTON")# buton yazısını yazdık
    buton.move(440,100)

    """

    """
    #pencerenin başlangıc konumunu(ilk 2 parametre) ve çözünürlüğünü verdik
    yazi = QtWidgets.QLabel(pencere)#qlabel oluşturarak pencere üzerine yerleştirdik
    yazi.setText("Bu bir deneme yazısı")#pencerede görünmesini istediğimiz yazıyı yazdık
    yazi.move(440,50)# yazımızı pixele göre hareket ettirdik
    resim = QtWidgets.QLabel(pencere)# resmimiz de pencere üzerine yerleştirdik
    resim.setPixmap(QtGui.QPixmap("fb.jpg"))#resim i set ettik 
    resim.move(2,90)

    """
    
    pencere.show()
    sys.exit(app.exec())#Pencerede çarpı butonuna basana kadar uygulama çalışacak yani standart bir uygulama gibi

Pencere()