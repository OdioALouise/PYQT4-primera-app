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

         editor = QSpinBox(parent)
         editor.setMinimum(0)
         editor.setMaximum(100)

         return editor

        

    def setEditorData(widgetEditor, qModelIndex):
        print "hola"
        
        
    def setModelData(widgetEditor, qAItemModel, qModelIndex):
        print "hola"
        

    def updateEditorGeometry(widgetEditor, qStyleOption, qModelindex):
        print "hola"
