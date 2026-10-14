import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from upload import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.adddig)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.calc)
        self.btn_eq.clicked.connect(self.avall)
        self.a = ''

    def adddig(self):
        s = self.sender().text()
        d = ''
        if s == '.':
            if s in self.a:
                return
        if self.a != '0':
            self.a += self.sender().text()
            self.table.display(self.a)
        else:
            self.a = s
            self.table.display(self.a)

    def calc(self):
        s = self.sender().text()
        if s in '+-*/':
            self.a += s
        elif s == 'btn_sqrt':
            self.a += '**0.5'
    def avall(self):
        s = eval(self.a)
        self.table.display(s)
        self.a = s



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
