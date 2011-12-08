from PyQt4 import QtCore, QtGui

import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    splitter = QtGui.QSplitter()

    sistemaArchivos = QtGui.QFileSystemModel()

    sistemaArchivos.setRootPath(QtCore.QDir.currentPath())

    arbol = QtGui.QTreeView(splitter)

    arbol.setModel(sistemaArchivos)

    arbol.setRootIndex(sistemaArchivos.index(QtCore.QDir.currentPath()))

    lista = QtGui.QListView(splitter)

    lista.setModel(sistemaArchivos)
    
    lista.setRootIndex(sistemaArchivos.index(QtCore.QDir.currentPath()));

    splitter.setWindowTitle("Primer ejemplo MVC")

    splitter.show()
    
    sys.exit(app.exec_())
