#Primera aplicacion  en python con pyqt
#Importamos la libreria del sistema, para conocer parámetros de arranque
#Importamos librerias de qt
import sys 
from PyQt4 import QtCore, QtGui


class dragBoton(QtGui.QPushButton):
        def __init__(self, title, parent):
                super(dragBoton, self).__init__(title, parent)
                 

        def mouseMoveEvent(self, e):
                
                mimedata = QtCore.QMimeData()

                self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
                                
                drag = QtGui.QDrag(self)
                                
                pixmap = QtGui.QPixmap("thumb_icon.png")
                                
                drag.setPixmap(pixmap)
                drag.setMimeData(mimedata)
                drag.setHotSpot(e.pos() - self.rect().topLeft())
                dropAction = drag.start(QtCore.Qt.MoveAction)

        def clickado(self):
                QtGui.QMessageBox.question(self, 'Mensaje', "¿Esta seguro de cerrar la aplicacion?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                self.setDisabled(True)

                

#Definimos una clase
#Forma de declarar una clase con herencia
class claseWidget(QtGui.QWidget):
        #Inicializacion
        def __init__(self):
                super(claseWidget, self).__init__()
                
                self.initUI()
                        
        def initUI(self):

                self.setAcceptDrops(True)

                iP = QtGui.QPixmap("thumb_icon.png")
                
                
                self.button = dragBoton('Boton', self)
                self.button.move(100, 65)
                


                self.button2 = dragBoton('', self)
                self.button2.move(100, 105)
                self.button2.setToolTip('Pozo')
                self.button2.setIcon(QtGui.QIcon('DotIcon.png'))
                self.button2.clicked.connect(self.button2.clickado)

                
        
                #Creamos un tooltip, primero seteamos sus valores por defecto
                QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
                self.setToolTip('Area del dominio')
                
                #Creamos un boton placebo
                btn = QtGui.QPushButton('Crear Dominio', self)
                btn.setToolTip('Botón para crear dominio')
                btn.resize(btn.sizeHint())
                btn.move(50, 50)
                
                #Creamos un botón para cerrar
                qbtn = QtGui.QPushButton('Quit', self)
                qbtn.resize(qbtn.sizeHint())
                qbtn.move(200, 200)
                QtCore.QObject.connect(qbtn, QtCore.SIGNAL('clicked()'), QtCore.QCoreApplication.instance().quit)
                                
                #Posicion, titulo e icono de la ventana por defecto
                self.setGeometry(250, 90, 500, 500)
                self.setWindowTitle('Icono')
                self.setWindowIcon(QtGui.QIcon('icon.png'))
                
                self.show()

        def closeEvent(self, event):
                
                reply = QtGui.QMessageBox.question(self, 'Mensaje', "¿Esta seguro de cerrar la aplicacion?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                        event.accept()
                else:
                        event.ignore()      

        def dragEnterEvent(self, e):
                
                e.accept()
                self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                

        def dropEvent(self, e):
                position = e.pos()
                self.button.move(position)

                e.setDropAction(QtCore.Qt.MoveAction)
                e.accept()
                
        
                
                                
def main():

         app = QtGui.QApplication(sys.argv)
         app.setStartDragDistance(100)
         """
         #Lo que hacemos aqui es comentar el widget anterior
         w = QtGui.QWidget()
         w.resize(250, 150)
         w.move(200, 300)
         w.setWindowTitle('Primer ejemplo')
         w.show()
         """
         ex = claseWidget()
         ex.show()
         app.exec_()
         sys.exit(app.exec_())
         
if __name__ == "__main__":
        main()
