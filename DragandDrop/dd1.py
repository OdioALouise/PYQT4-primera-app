#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this program, we can press
on a button with a left mouse
click or drag and drop the button 
with  the right mouse click. 

author: Jan Bodnar
website: zetcode.com
last edited: December 2010
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Button(QtGui.QPushButton):
 
    iconoUrl = "" 
 
  
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, e):

        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()
 
        drag = QtGui.QDrag(self)
                                
        pixmap = QtGui.QPixmap(self.iconoUrl)

        drag = QtGui.QDrag(self)
        drag.setPixmap(pixmap)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
 

        dropAction = drag.start(QtCore.Qt.MoveAction)


    def mousePressEvent(self, e):
      
        QtGui.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
 
            print 'press' + self.iconoUrl
 


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
        
    def initUI(self):

        self.setAcceptDrops(True)

 
        self.button = Button('Button2', self)
        self.button.iconoUrl = "DotIcon.png"
        self.button.move(100, 65)

        self.button2 = Button('Button1', self)
        self.button2.iconoUrl = "thumb_icon.png"
        self.button2.move(100, 105)

        
 
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
      
        e.accept()

    def dropEvent(self, e):

        position = e.pos()
        #self.button.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()

def main():
  
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()  


if __name__ == '__main__':
    main()
