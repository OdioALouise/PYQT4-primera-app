from PyQt4 import QtCore, QtGui
import sys

class modelo(QtCore.QAbstractItemModel):

    def __init__(self):
        atributo1 = "atributo11"
        atributo2 = "atributo22"
        lista = []
        lista.append(atributo1)
        lista.append(atributo2)
        
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.lista)


    def data(self, index, role):

        if role==QtCore.Qt.ToolTipRole:
            return "Codigo Hex: " + self.lista[index.row()].name()

       
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.lista[row]
            return value.name()            


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

    data= QtCore.QStringList()
    data << "uno" << "dos"
    
    m = modelo()

    """
    dialog = dialogo()
    dialog.open()
    """
    vista1=QtGui.QListView()
    
    vista1.show()

    vista1.setModel(data)


    sys.exit(app.exec_())

    
