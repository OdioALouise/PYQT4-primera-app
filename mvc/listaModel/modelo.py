from PyQt4 import QtCore, QtGui

class modelo(QtCore.QAbstractItemModel):
    atributo1 = "atributo11"
    atributo2 = "atributo22"

    def __init__(self):
        print "Objeto creado"


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


if __name__ == "__main__":

    dd = "objeto"
    d = delegado(dd)

    print "hola"
