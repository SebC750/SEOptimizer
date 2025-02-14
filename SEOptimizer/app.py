from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from views.login import LoginWindow

app = QApplication([])

def main():
    main_window = LoginWindow()
    app.exec()

if __name__ == "__main__":
    main()
