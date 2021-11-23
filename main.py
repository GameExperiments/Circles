import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        """Закрытие окна при нажатии на крестик"""
        self.setWindowTitle('Круги')
        self.pushButton.clicked.connect(self.on_pushbutton_clicked)
    
    def on_pushbutton_clicked(self):
        x = random.randint(0, 300)
        y = random.randint(0, 150)
        high = random.randint(50, 150)
        try:
            self.scene.addEllipse(x, y, high, high, pen=QColor(0, 0, 0), brush=QColor(255, 255, 0))
        except Exception:
            self.scene = QGraphicsScene()
            self.scene.setSceneRect(0, 0, 350, 195)
            self.graphicsView.setScene(self.scene)
            self.scene.addEllipse(x, y, high, high, pen=QColor(0, 0, 0), brush=QColor(255, 255, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
