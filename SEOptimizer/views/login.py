from PySide6.QtWidgets import QWidget, QMainWindow,QGroupBox, QLabel,QPushButton


class LoginWindow(QMainWindow):
    def __init__(self):
         super().__init__()
         self.setWindowTitle("SEOptimizer")
         self.root = QWidget()
         self.setGeometry(300, 100, 500, 500)
         self.button = QPushButton("Hello world!")
         self.button.setStyle("")
         self.setCentralWidget(self.button)
         self.show()