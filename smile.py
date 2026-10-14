import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


from nasroenie import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.verticalSlider.valueChanged.connect(self.size)
        self.draw = None

        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(50)
    def size(self):
        self.draw = True
        self.update()
    def paintEvent(self, event):
        if self.draw:
            qt = QPainter()
            qt.begin(self)
            self.draw_s(qt)
            qt.end()
    def draw_s(self, qt):
        k = self.verticalSlider.value()
        qt.setPen(QColor(255,0,0,))
        k = self.verticalSlider.value()
        print(k)
        qt.drawEllipse(0, 0, 10 * k, 10 * k )
        self.draw =False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())