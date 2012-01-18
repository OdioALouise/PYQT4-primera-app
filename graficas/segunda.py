from PyQt4.QtGui import *
from PyQt4.QtCore import *

import numpy as np
import sys


class vista(QGraphicsView):
	def __init__(self, parent):
		super(vista, self).__init__(parent)
		self.boton = boton("Hola", self)
		self.setGeometry(10,10, 250, 250)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, e):
		e.accept()

	def dropEvent(self, e):
		position = e.pos()
		self.boton.move(position)
		
		e.setDropAction(Qt.MoveAction)
		e.accept()

class boton(QPushButton):

	iconoUrl = ""

	def __init__(self, title, parent):
		super(boton, self).__init__(title, parent)

	def mouseMoveEvent(self, e):

		if e.buttons() == Qt.RightButton:
			return

		mimeData = QMimeData()
 
		drag = QDrag(self)

		pixmap = QPixmap(self.iconoUrl)

		drag = QDrag(self)
		drag.setPixmap(pixmap)
		drag.setMimeData(mimeData)
		drag.setHotSpot(e.pos() - self.rect().topLeft())

		dropAction = drag.start(Qt.MoveAction)

	def mousePressEvent(self, e):
		QPushButton.mousePressEvent(self, e)

class Example(QWidget):

	def __init__(self):
		super(Example, self).__init__()
		self.setAcceptDrops(True)



if __name__ == "__main__":

	app = QApplication(sys.argv)

	ex = Example()

	vista = vista(ex)

	ex.show()


	sys.exit(app.exec_())
