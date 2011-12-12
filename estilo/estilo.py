from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class widget(QWidget):

    def __init__(self):
        super(widget, self).__init__()
        self.init()

    def init(self):
        self.setWindowTitle("Widget principal")

        self.setGeometry(100, 50, 800, 600)
        
        self.dominio = widgetDominio(self)

        self.dominio.show()

        
class widgetDominio(QWidget):

    def __init__(self, padre):

        super(widgetDominio, self).__init__(parent = padre)
        self.init()

    def init(self):
        self.setGeometry(100, 100, 400, 400)

        self.grilla = QGridLayout()

        lineedit = QLineEdit()
        lineedit.__init__("Hola Mundo", parent = self)
        
        self.grilla.addWidget(lineedit, 0, 0)
                
        boton = QPushButton()
        boton.__init__("Otro ejemplo", parent = self)
        boton.move(50, 50)

        self.grilla.addWidget(boton, 0, 2)        

        self.setContentsMargins(-1, 20, 10, -1)

        self.setLayout(self.grilla)   
        
        self.setStyleSheet("QWidget {margin: 5px; \n"                           
                           "background-color: red}")        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widgetPrincipal = widget()

    widgetPrincipal.show()

    sys.exit(app.exec_())
    
