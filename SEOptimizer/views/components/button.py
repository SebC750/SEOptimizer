from PySide6.QtWidgets import QWidget, QPalette, QPushButton


class Button(QWidget):
    def __init__(self, color, text):
        self.setAutoFillBackground(True)
        self.button = QPushButton(text)
        self.
        