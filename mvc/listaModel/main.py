from PyQt4 import QtGui, QtCore
import sys
import modelo

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    numeros = QtCore.QStringList()
    numeros << "Uno" << "Dos" << "Tres"

    #modelo = QtCore.QAbstractItemModel()
    
    model = QtGui.QStringListModel(numeros)

    m = modelo.modelo()

    print m.atributo1
    print m.atributo2

    vista = QtGui.QListView()
    vista.setModel(model)
    vista.show()



    
    
    sys.exit(app.exec_())
