# -*- coding: utf-8 -*
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QTextEdit,QLineEdit
from PyQt5.QtWidgets import QMainWindow , QFormLayout , QLabel
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Ana_Pencere(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("deneme")

    def init_ui(self):
        self.pencere1 = QWidget()
        self.pencere1_tasarım()
        
        self.pencere1.setWindowTitle("deneme")
        
        self.setCentralWidget(self.pencere1)
        self.show()
        
    
    def pencere1_tasarım(self):
        form = QFormLayout()
        self.kullanici_mail = QLineEdit()
        form.addRow(QLabel("Mail Adresiniz:"),self.kullanici_mail)
        self.pencere1.setWindowTitle("deneme")
        
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)     
        form.addRow(QLabel("Şifreniz:"),self.parola)
        
        
        self.gonderilen_mail = QLineEdit()
        form.addRow(QLabel("Kime:"),self.gonderilen_mail)
        
        self.konu = QLineEdit()
        form.addRow(QLabel("Konu:"),self.konu)
        
        self.ileti = QTextEdit()
        form.addRow(QLabel("İleti:"),self.ileti)
        
        self.gonder = QPushButton("Gönder")
        self.gonder.clicked.connect(self.gonder_clk)
        
        form.addWidget(self.gonder)
        
        
        self.pencere1.setLayout(form)
        
    
    def gonder_clk(self):
        mesaj = MIMEMultipart()
            
        mesaj["From"] = self.kullanici_mail .text()  # Kimden Göndereceğimiz

        mesaj["To"] = self.gonderilen_mail.text()  # Kime Göndereceğimiz

        mesaj["Subject"] = self.konu.text()  # Mailimizin Konusu
            
        yazi = self.ileti.toPlainText()
            
        mesaj_govdesi = MIMEText(yazi,"plain") # Mailimizin gövdesini bu sınıftan oluşturuyoruz.
        mesaj.attach(mesaj_govdesi)  # Mailimizin gövdesini bu sınıftan oluşturuyoruz.
                
        try:       
            mail = smtplib.SMTP("smtp.live.com",587)  # SMTP objemizi oluşturuyoruz ve hotmail smtp server'ına bağlanıyoruz.

            mail.ehlo() # SMTP serverına kendimizi tanıtıyoruz.
 
            mail.starttls() # Adresimizin ve Parolamızın şifrelenmesi için gerekli

            mail.login(self.kullanici_mail.text(),self.parola.text()) # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.

            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())  # Mailimizi gönderiyoruz.
            print("Mail başarıyla gönderildi....")
            self.mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

        except:
            sys.stderr.write("Mail Gönderme Başarısız Oldu!")
            sys.stderr.flush()
    

       
app = QApplication(sys.argv)

ana_pencere = Ana_Pencere()

sys.exit(app.exec_())



