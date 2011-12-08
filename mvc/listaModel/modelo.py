from PyQt4 import QtCore, QtGui

class modelo(QtCore.QAbstractItemModel):
    atributo1 = "atributo11"
    atributo2 = "atributo22"

    def __init__(self):
        print "Objeto creado"


class delegado(QtGui.QAbstractItemDelegate):
    Q_OBJECT

    def __init__(self, qobjet):
        print "hola"

    def createEditor(parentWidget, qstyleOption, qModelIndex):
        

    def setEditorData(widgetEditor, qModelIndex):
        
        
    def setModelData(widgetEditor, qAItemModel, qModelIndex):
        

    def updateEditorGeometry(widgetEditor, qStyleOption, qModelindex):
        
