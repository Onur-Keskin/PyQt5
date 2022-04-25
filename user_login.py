import  sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()

        self.init_ui()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")


        self.baglanti.commit()

    def init_ui(self):

        self.kullanici_adi =  QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        self.register = QtWidgets.QPushButton("Kayıt Ol")
        


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.register)


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.click)
        self.register.clicked.connect(self.click)

        self.show()
  

    def click(self):
        sender = self.sender()

        if sender.text() == "Giriş Yap":
            adi = self.kullanici_adi.text()
            par = self.parola.text()

            self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))

            data = self.cursor.fetchall()#fetchall fonksiyonu bir liste döndürür.

            if len(data) == 0:
                self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
            else:
                self.yazi_alani.setText("Hoşgeldiniz " + adi)
            

        else:
            adi = self.kullanici_adi.text()
            par = self.parola.text()
            
            sorgu = "Insert into üyeler Values(?,?)"
            
            self.cursor.execute(sorgu,(adi,par))
            
            self.yazi_alani.setText("Başarıyla Kayıt Olundu!")
            
            self.baglanti.commit()
            
           
            
            
            


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
