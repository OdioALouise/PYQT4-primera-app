import sys, random
from PyQt4 import QtCore, QtGui 

class claseWidget(QtGui.QWidget):

        def __init__(self):
                super(claseWidget, self).__init__()
                self.inicializacion()

        def inicializacion(self):
                self.setWindowTitle('Ejemplo con Painter')

        def paintEvent(self, event):
                painter = QtGui.QPainter()

                painter.begin(self)
                painter.setPen(QtCore.Qt.blue)

                size = self.size()
                """
                for i in range(10):
                        x = random.randint(1, size.width()-1)
                        y = random.randint(1, size.height()-1)
                        painter.drawPoint(x, y)     
                
                painter.drawPoint(50, 88)
                painter.drawPoint(70, 88)
                """
                
                painter.drawLine(50, 88, 70, 88)
                target = QtCore.QRectF(10.0, 20.0, 80.0, 60.0);
                source = QtCore.QRectF(0.0, 0.0, 70.0, 40.0);
                pixmap = QtGui.QPixmap("DotIcon.png")


                painter.drawPixmap(target, pixmap, source)
                painter.end()

def main():
        app = QtGui.QApplication(sys.argv)

        wdg = claseWidget()
        wdg.show()      
        
        app.exec_()
        sys.exit(app.exec_())
        
if __name__ == "__main__":
        main()
