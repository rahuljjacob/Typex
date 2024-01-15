from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Typex")

        self.plaintext = QLineEdit()
        self.rotor1pos = QLineEdit()
        self.rotor2pos = QLineEdit()
        self.rotor3pos = QLineEdit()

        self.label = QLabel()

        button = QPushButton("Encrypt")
        button.setFixedSize(QSize(80, 40))
        button.setCheckable(True)
        button.clicked.connect(self.encrypt)

        layout = QVBoxLayout()
        layout.addWidget(self.plaintext)
        layout.addWidget(self.rotor1pos)
        layout.addWidget(self.rotor2pos)
        layout.addWidget(self.rotor3pos)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        

        self.setCentralWidget(container)

    def encrypt(self):
        self.label.setText(encrypt_decrypt.totalencryption(self.plaintext, ))
    

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
