import encrypt_decrypt
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QFormLayout, QHBoxLayout, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Typex")

        self.enc = QLabel()
        self.enc.setText("Encryption")

        self.plaintext = QLineEdit()
        self.encrotor1pos = QSpinBox()
        self.encrotor2pos = QSpinBox()
        self.encrotor3pos = QSpinBox()

        self.encrotorlayout = QHBoxLayout()
        self.encrotorlayout.addWidget(self.encrotor1pos)
        self.encrotorlayout.addWidget(self.encrotor2pos)
        self.encrotorlayout.addWidget(self.encrotor3pos)
        
        self.encbutton = QPushButton("Encrypt")
        self.encbutton.setFixedSize(QSize(80, 40))
        self.encbutton.setCheckable(True)
        self.encbutton.clicked.connect(self.encrypt)

        self.ciphertextout = QLabel()

        
        layout = QVBoxLayout()
        layout.addWidget(self.enc)
        layout.addWidget(self.plaintext)
        layout.addLayout(self.encrotorlayout)
        layout.addWidget(self.encbutton)
        layout.addWidget(self.ciphertextout)


        self.dec = QLabel()

        self.dec.setText("Decryption")

        self.ciphertext = QLineEdit()
        self.decrotor1pos = QSpinBox()
        self.decrotor2pos = QSpinBox()
        self.decrotor3pos = QSpinBox()

        self.decrotorlayout = QHBoxLayout()
        self.decrotorlayout.addWidget(self.decrotor1pos)
        self.decrotorlayout.addWidget(self.decrotor2pos)
        self.decrotorlayout.addWidget(self.decrotor3pos)
        

        self.plaintextout= QLabel()

        self.decbutton = QPushButton("Decrypt")
        self.decbutton.setFixedSize(QSize(80, 40))
        self.decbutton.setCheckable(True)
        self.decbutton.clicked.connect(self.decrypt)

        layout2 = QVBoxLayout()
        layout2.addWidget(self.dec)
        layout.addWidget(self.ciphertext)
        layout2.addLayout(self.decrotorlayout)
        layout2.addWidget(self.decbutton)
        layout2.addWidget(self.plaintextout)

        finallayout = QVBoxLayout()
        finallayout.addLayout(layout)
        finallayout.addLayout(layout2)
    
        container = QWidget()
        container.setLayout(finallayout)

        self.setCentralWidget(container)


    def encrypt(self):
        plaintext = self.plaintext.text()
        ciphertext = encrypt_decrypt.totalencryption(plaintext, [self.encrotor1pos.value(), self.encrotor2pos.value(), self.encrotor3pos.value()])
        self.ciphertextout.setText(ciphertext)


    def decrypt(self):
        ciphertext = self.plaintext.text()
        plaintext = encrypt_decrypt.totaldecryption(ciphertext, [self.decrotor1pos.value(), self.decrotor2pos.value(), self.decrotor3pos.value()])
        self.plaintextout.setText(plaintext)
    

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
