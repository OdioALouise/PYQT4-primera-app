from PyQt4 import QtCore, QtGui
import sys


class equipo(object):
    def __init__(self, nombre, asociacion):
        self.nombre = nombre
        self.asociacion = asociacion
    """
    def __init__(self):
        self.nombre = "Natalia Natalia"
        self.asociacion = "Natalia Natalia"
    """
        

class modelo(QtCore.QAbstractItemModel):

    def __init__(self, parent = None):
        super(modelo, self).__init__(parent)

        self.lista = []

        for nombre, asociacion in (
            ("Rampla Juniors", "AUF"),
            ("Los Sauces", "OFI"),
            ("Tacuarembo FC", "AUF")):
            self.lista.append(equipo(nombre, asociacion))


        
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.lista)

    def columnCount(self, parent = QtCore.QModelIndex()):
        return 0

    def data(self, index, role):

        if role==QtCore.Qt.ToolTipRole:

            valor = self.lista[index.row()]
                       
            return "Codigo Hex: " + QtCore.QVariant(valor.asociacion).toString()

       
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
          
            value = self.lista[row]

            return QtCore.QVariant(value.nombre)

    def index(row, column, parent = QtCore.QModelIndex()):
        return QtCore.QAbstractItemModel.createIndex(row, column, object = 0)


class delegado(QtGui.QAbstractItemDelegate):

    Q_OBJECT = ""

    def __init__(self, qobjet):
        print "hola"

    def createEditor(parentWidget, qstyleOption, qModelIndex):

         editor = QtGui.QSpinBox(parentWidget)
         editor.setMinimum(0)
         editor.setMaximum(100)

         return editor

        

    def setEditorData(widgetEditor, qModelIndex):
        value = qModelIndex.model().data(qModelIndex, QtCore.Qt.EditRole).toInt()
        spinBox = QtGui.QSpinBox(widgetEditor);
        spinBox.setValue(value);


    def setModelData(widgetEditor, qAItemModel, qModelIndex):
        print "hola"
        

    def updateEditorGeometry(widgetEditor, qStyleOption, qModelindex):
        print "hola"

class dialogo(QtGui.QDialog):
    def __init__(self):
        super(dialogo, self).__init__(parent = None)
        self.init()

    def init(self):
        self.setWindowTitle("Dialogo")
        self.setGeometry(250, 90, 500, 500)

        self.address = QtGui.QLineEdit("Escriba su direccion", parent = self)
        self.address.setMaxLength(20)
        self.address.move(90, 100)

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    m = modelo()


    i = 0
    
    for i in range(m.rowCount()):

       indice = m.index(i, m.columnCount()) 

       valor = m.data(indice, role = QtCore.Qt.DisplayRole)

       print valor.toString()
    
    """
    dialog = dialogo()
    dialog.open()
    """
    vista1 = QtGui.QTreeView()
    
    vista1.show()

    vista1.setModel(m)


    sys.exit(app.exec_())

    
