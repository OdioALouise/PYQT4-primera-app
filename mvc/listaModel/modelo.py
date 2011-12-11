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
            ("Tacuarembo FC", "AUF"),
            ("Sportivo San Felix", "Surena")):
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

    def index(self, row, column, parent = QtCore.QModelIndex()):
        
        return self.createIndex(row, column, 0)

    def parent(self, hijo):            

        child_id = hijo.internalId()
        print child_id

        #if child_id == 0:
        return QtCore.QModelIndex()
        """
        item_id = self.parent_ids[child_id]
        
        if item_id == 0 :
            return self.createIndex(0, 0, item_id)

        parent_id = self.parent_ids[item_id]
        
        row = self.dir_children_ids[parent_id].index(item_id)
        
        return self.createIndex(row, 0, item_id)
        """

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
    
    
    #dialog = dialogo()
      
    #dialog.open()
    
    vista2 = QtGui.QTableView()
    
    vista1 = QtGui.QTreeView()

    vista3 = QtGui.QListView()

    vista1.setModel(m)

    vista2.setModel(m)

    vista3.setModel(m)
    
    vista1.show()

    vista2.show()

    vista3.show()



    sys.exit(app.exec_())

    
