import sys
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QColor

from PIL import Ui_MainWindow
from PyQt6.QtCore import Qt, QPoint


class MyPillow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname, _ = QFileDialog.getOpenFileName(
            self,
            'Выбрать картинку',
            '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)'
        )

        self.pixmap = QPixmap(self.fname)  # Загружаем картинку
        self.scaled = self.pixmap.scaled(
            350, 350,
            Qt.AspectRatioMode.KeepAspectRatio,  # Сохраняем пропорции
            Qt.TransformationMode.SmoothTransformation)
        # Качественное масштабирование
        self.scaled = QImage(self.scaled)
        self.pixmap = QPixmap.fromImage(self.scaled)

        self.image.setPixmap(self.pixmap)
        self.copy_img = self.scaled.copy()
        for i in self.channelButtons.buttons():
            i.clicked.connect(self.run)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.copy_img = self.scaled.copy()
        x, y = self.copy_img.size().width(), self.copy_img.size().height()
        for i in range(x):
            for j in range(y):

                r, g, b, e = self.copy_img.pixelColor(i, j).getRgb()
                print(r, g, b)
                if self.sender().text() == 'Красный':
                    print(type(self.copy_img), i, j)
                    self.copy_img.setPixelColor(QPoint(i, j), QColor(r,0,0))
        self.pixmap = QPixmap.fromImage(self.copy_img)
        self.image.setPixmap(self.copy_img)


def except_hook(cls, exception, trader):
    sys.__excepthook__(cls, exception, trader)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
