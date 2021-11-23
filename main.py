import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QMainWindow

from UI import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushbutton_clicked)
    
    def on_pushbutton_clicked(self):
        x = random.randint(0, 300)
        y = random.randint(0, 150)
        high = random.randint(50, 150)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        penr = 255 - r
        peng = 255 - g
        penb = 255 - b
        try:
            self.scene.addEllipse(x, y, high, high, pen=QColor(penr, peng, penb), brush=QColor(r, g, b))
        except Exception:
            self.scene = QGraphicsScene()
            self.scene.setSceneRect(0, 0, 350, 195)
            self.graphicsView.setScene(self.scene)
            self.scene.addEllipse(x, y, high, high, pen=QColor(penr, peng, penb), brush=QColor(r, g, b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())