import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore
import random


class Circle:
    def __init__(self, cx):
        self.cx = cx

    def vibor(self):
        return random.choice(self.cx)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Git и желтые окружности"
        left = 500
        top = 200
        width = 500
        height = 400
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)

        button = QPushButton("Add", self)
        button.setGeometry(QRect(200, 0, 50, 28))
        button.clicked.connect(self.paintcircle)

        self.should_paint_circle = False
        self.show()

    def paintEvent(self, event):
        super().paintEvent(event)
        c = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
             'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            b = Circle(c)
            painter.setBrush(QColor(b.vibor()))
            radiuse = random.randint(10, 100)
            painter.drawEllipse(200, 150, radiuse, radiuse)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


app = QApplication(sys.argv)
circle = Window()
circle.show()
sys.exit(app.exec_())
