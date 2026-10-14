import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('upload.ui', self)  # Одна строка — и всё работает!
        

    def run(self):
        self.label.setText("OK")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())