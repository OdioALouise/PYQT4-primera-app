import sys, random
from PyQt4 import QtCore, QtGui 

class claseWidget(QtGui.QWidget):

        simbolo = 0

        coordenada = QtCore.QPoint(0, 0)

        
         
        def __init__(self):
                super(claseWidget, self).__init__()
                self.inicializacion()

        def inicializacion(self):
                self.setWindowTitle('Ejemplo con Painter')

        def paintEvent(self, event):
                painter = QtGui.QPainter()
                painter.begin(self)
                painter.setPen(QtCore.Qt.blue)

                if(self.simbolo == 1):
                        print "Es uno"
                        #painter.drawLine(50, 88, 70, 88)
                        #target = QtCore.QRectF(self.coordenada.x(), self.coordenada.y(), 80.0, 60.0);
                        #source = QtCore.QRectF(0.0, 0.0, 70.0, 40.0);
                        
                        self.pixmap = QtGui.QPixmap("DotIcon.png")

                        #painter.drawPixmap(target, pixmap, source)
                        painter.drawPixmap(self.coordenada, self.pixmap)
                painter.end()

        def mousePressEvent(self, e):
                if e.button() == QtCore.Qt.LeftButton:
                        self.paintEvent(self)
                        posicion = e.pos()

                        self.coordenada.setX(posicion.x())
                        self.coordenada.setY(posicion.y())

                        self.simbolo = 1

                        self.clearFocus()


def main():
        app = QtGui.QApplication(sys.argv)

        wdg = claseWidget()
        wdg.show()      
        
        app.exec_()
        sys.exit(app.exec_())
        
if __name__ == "__main__":
        main()
