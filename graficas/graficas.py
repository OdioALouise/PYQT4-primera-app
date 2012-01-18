from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import sys

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

sys.path.append("models")

import barrera, pozo, controlador


# 01 ELEMENTO DOMINIO


class elementoDominio(object):

    elementoDominio = 0

    existe = False

    idElemento = 1000

    reloj = False

    transicion = False

    ContEnsayo = ""

    menuMouse = ""

    selectedMenuMouse = {}

    gbCoord = ""

    Dominio = ""

    #Pozo candidato a ser agregado
    pozoCandidato = ""
    hayPozoCandidato = False

    pozoSeleccionado = 0

    
    def __init__(self):
        super(elementoDominio, self).__init__()


# 02 BOTON

class boton(QPushButton):

	global elementoDominio

	id = 1000  

	posicion = 0

	accionCoord = {}

	def __init__(self, icono, texto, padre, tooltip):
		super(boton, self).__init__(icono, texto, padre)
		self.init(tooltip)

	def init(self, tooltip):

		#Seteo inicial del boton
		self.setAcceptDrops(True)        
		self.tooltip = tooltip       
		self.setGeometry(QRect(50, 20, 41, 23))
		self.setCursor(QCursor(Qt.OpenHandCursor))
		self.setMouseTracking(True)
		self.setToolTip(QApplication.translate("Form", tooltip, None, QApplication.UnicodeUTF8))

	def mousePressEvent(self, e):

		if e.button() == Qt.LeftButton:

			#Cambiamos el cursor, y luego procedemos a evaluar estado del reloj
			#Si no existe creamos un temporizador, cuando alcanze el tiempo dado
			#el usuario va a poder arrastrar el boton.
			self.setCursor(QCursor(Qt.ClosedHandCursor))

			if self.id == 1000:
				#elementoDominio.gbCoord.setPozo()

				#Volvemos al color normal del pozo seleccionado
				for boton in elementoDominio.Dominio.botones:
					boton.setIcon(QIcon("content/images/blackDotIcon.png"))

			elif self.id == 1001:
				#elementoDominio.gbCoord.setRecta()
				pass

			if elementoDominio.reloj == False:
				reloj = QTimer()
				reloj.singleShot(800, self.apagar)
				elementoDominio.transicion = True
				elementoDominio.reloj = True

			if self.id != 1000 and self.id != 1001:                
				#Se muestran sus coordenadas
				#elementoDominio.gbCoord.setPozoExistente(self.id)

				#elementoDominio.pozoSeleccionado = self.id
				#elementoDominio.gbCoord.actualizarCoordenadasPozo(self.id)
				elementoDominio.Dominio.rectaSeleccionada['id'] = 0 

				for pozo in elementoDominio.Dominio.botones:
					if pozo.id != self.id:
						pozo.setIcon(QIcon("content/images/blackDotIcon.png"))
				self.setIcon(QIcon("content/images/redDotIcon.png"))

			else:
				#Reseteo de recta seleccionada
				elementoDominio.Dominio.rectaSeleccionada['id'] = 0
				self.update()
				#elementoDominio.gbCoord.eliminarPlacebos()

		else:
			elementoDominio.selectedMenuMouse["tipo"] = "punto"
			elementoDominio.selectedMenuMouse["id"] = self.id

			elementoDominio.menuMouse.move(self.pos())

			elementoDominio.menuMouse.show()

	def mouseMoveEvent(self, e):
		#Evaluacion que se entiende como, 'El usuario puede comenzar a arrastrar el boton'
		if elementoDominio.reloj == True and elementoDominio.transicion == False:
			self.setCursor(QCursor(Qt.OpenHandCursor))
			mimedata = QMimeData()                             
			drag = QDrag(self)

			#Sentencia que representa en el margen superior
			#izquierdo del mouse al elemento que esta siendo
			#arrastrado por la ventana.

			if self.tooltip == "pozo":
				pixmap = QPixmap("content/images/blackDotIcon.png")
				drag.setPixmap(pixmap)
				elementoDominio.elementoDominio = 0
			else:
				pixmap = QPixmap("content/images/blackBarrera.png")
				drag.setPixmap(pixmap)
				elementoDominio.elementoDominio = 1


			#Como se describiese en la enunciacion de la clase elementoDominio
			# se evalua si el elemento es nuevo o ya existe en el dominio.
			#dependiendo de la evaluacion el atrinuto existe sera verdadero o falso

			if self.id == 1000 or self.id == 1001:           
				elementoDominio.existe = False  
			else:
				elementoDominio.existe = True

			elementoDominio.idElemento = self.id

			drag.setMimeData(mimedata)
			drag.setHotSpot(e.pos() - self.rect().topLeft())
			dropAction = drag.start(Qt.MoveAction)

		if self.id != 1000 and self.id != 1001:
			#Se muestran sus coordenadas
			#elementoDominio.gbCoord.setPozoExistente(self.id)
			pass

	def apagar(self):
		elementoDominio.transicion = False

	#Cuando se suelta el mouse luego de un arrastre
	#incondicionalmente se setean las banderas globales con los siguientes
	#valores
	def mouseReleaseEvent(self, e):        
		elementoDominio.transicion = False
		elementoDominio.reloj = False
		self.setCursor(QCursor(Qt.OpenHandCursor))

#03 COORDENADAS
"""
class gbCoordenadas(QGroupBox):
    def __init__(self, padre):
        super(gbCoordenadas, self).__init__(padre)
        self.init()

    def init(self):
        self.setGeometry(QRect(260, 110, 151, 181))
        self.setTitle("Coordenadas")

        #Etiqueta de Tipo 
        self.label = QLabel(self)
        self.label.setGeometry(QRect(10, 20, 91, 16))
        self.label.setText(QApplication.translate("Form", "Recta Pozo", None, QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setVisible(False)

        #X1
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(40, 50, 25, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QRect(100, 50, 25, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QRect(40, 100, 25, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QRect(100, 100, 25, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(10, 50, 25, 20))
        self.label_2.setText("X1")
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setVisible(False)


        #Y1
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(75, 50, 25, 20))
        self.label_3.setText("Y1")
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setVisible(False)


        #X2
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(10, 100, 25, 20))
        self.label_4.setText("X2")
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setVisible(False)

        #Y2
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(75, 100, 25, 20))
        self.label_5.setText("Y2")
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setVisible(False)
        
        #Combo box
        self.cbTipo = QComboBox( self )
        self.cbTipo.setGeometry(QRect(60,20, 60, 20))
        listaStrings = QStringList()
        listaStrings << "Negativo" << "Positivo"
        
        self.cbTipo.addItems(listaStrings)
        self.cbTipo.setVisible(False)
        


        #Boton Aceptar
        self.btnAceptar = QPushButton(self)
        self.btnAceptar.setGeometry(QRect(10, 155, 50, 20))
        self.btnAceptar.setText("Aceptar")
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar = QPushButton(self)
        self.btnCancelar.setGeometry(QRect(80, 155, 50, 20))
        self.btnCancelar.setText("Cancelar")
        self.btnCancelar.setVisible(False)

        #Boton de Vista Previa
        self.btnPrevia = QPushButton(self)
        self.btnPrevia.setGeometry(QRect(10, 130, 100, 20))
        self.btnPrevia.setText("Vista Previa")
        self.btnPrevia.setVisible(False)

        #Boton Actualizar
        self.btnActualizar = QPushButton(self)
        self.btnActualizar.setGeometry(QRect(10,130, 100, 20))
        self.btnActualizar.setText("Actualizar")
        self.btnActualizar.setVisible(False)

        QObject.connect(self.btnAceptar, SIGNAL('clicked()'), self.setAceptar)
        QObject.connect(self.btnCancelar, SIGNAL('clicked()'), self.setCancelar)
        QObject.connect(self.btnPrevia, SIGNAL('clicked()'), self.setPrevia)
        QObject.connect(self.btnActualizar, SIGNAL('clicked()'), self.setActualizar)

        #Validacion
        self.validador = QIntValidator(-100, 900, self)

        self.lineEdit.setValidator(self.validador)
        self.lineEdit_2.setValidator(self.validador)
        self.lineEdit_3.setValidator(self.validador)
        self.lineEdit_4.setValidator(self.validador)
        
    def setPozo(self):
        #Etiqueta de Tipo 
        self.label.setText(QApplication.translate("Form", "Pozo", None, QApplication.UnicodeUTF8))
        self.label.setVisible(True)

        #X1
        self.lineEdit.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit.setVisible(True)

        #Y1
        self.lineEdit_2.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_2.setVisible(True)

        #X2
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(True)


        #Y1
        self.label_3.setVisible(True)


        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)
    
        #Combo
        self.cbTipo.setVisible(False)

        #Boton Aceptar
        self.btnAceptar.setVisible(True)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(True)

        #Vista Previa
        self.btnPrevia.setVisible(True)

        #Boton Actualizar
        self.btnActualizar.setVisible(False)

    def setRecta(self):
        #Etiqueta de Tipo 
        self.label.setText(QApplication.translate("Form", "Recta", None, QApplication.UnicodeUTF8))
        self.label.setVisible(True)

        #X1
        self.lineEdit.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit.setVisible(True)

        #Y1
        self.lineEdit_2.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_2.setVisible(True)

        #X2
        self.lineEdit_3.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_3.setVisible(True)

        #Y2
        self.lineEdit_4.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_4.setVisible(True)

        #X1
        self.label_2.setVisible(True)


        #Y1
        self.label_3.setVisible(True)


        #X2
        self.label_4.setVisible(True)

        #Y2
        self.label_5.setVisible(True)

        #Combo
        self.cbTipo.setVisible(True)


        #Boton Aceptar
        self.btnAceptar.setVisible(True)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(True)

        #Vista Previa
        self.btnPrevia.setVisible(True)

        #Boton Actualizar
        self.btnActualizar.setVisible(False)
        
    def setAceptar(self):

        if self.label.text() == "Pozo":

            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
                if not elementoDominio.hayPozoCandidato:
                    elementoDominio.pozoCandidato = QPushButton(elementoDominio.Dominio)
                    elementoDominio.hayPozoCandidato = True
                    elementoDominio.pozoCandidato.setGeometry(QRect(np.int32(self.lineEdit.text()),
                                                                           np.int32(self.lineEdit_2.text()), 25, 20))
                    elementoDominio.pozoCandidato.show()
                            
            
                b = boton(QIcon("content/images/blackDotIcon.png"), "", elementoDominio.Dominio, "pozo")

                b.id = elementoDominio.ContEnsayo.agregarPozo(elementoDominio.pozoCandidato.x(), elementoDominio.pozoCandidato.y())                

                elementoDominio.Dominio.botones.append(b)

                b.show()
                elementoDominio.pozoCandidato.hide()
                elementoDominio.pozoCandidato = None
                elementoDominio.hayPozoCandidato = False

            

        else:                                   
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text()!= "" and self.lineEdit_4.text() != "":
                if not elementoDominio.ContEnsayo.hayRectaCandidata():
                    elementoDominio.ContEnsayo.agregarRecta(self.cbTipo.currentText(), 
np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
                                                                     np.int32(self.lineEdit_4.text()))
                else:
                    elementoDominio.ContEnsayo.incluirCandidata(self.cbTipo.currentText())

                self.update()
                
        #Reseteo de recta seleccionada
        elementoDominio.Dominio.rectaSeleccionada['id'] = 0
        self.update()

        #Etiqueta de Tipo 
        self.label.setText(QApplication.translate("Form", "Recta", None, QApplication.UnicodeUTF8))
        self.label.setVisible(False)

        #X1
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(False)


        #Y1
        self.label_3.setVisible(False)


        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)

        #Combo
        self.cbTipo.setVisible(False)

        #Boton Aceptar
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)

        
    def setCancelar(self):
        
        #Etiqueta de Tipo 
        self.label.setText(QApplication.translate("Form", "Recta", None, QApplication.UnicodeUTF8))
        self.label.setVisible(False)

        #X1
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(False)

        #Y1
        self.label_3.setVisible(False)


        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)

        #Combo
        self.cbTipo.setVisible(False)

        #Boton Aceptar
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)


        if elementoDominio.ContEnsayo.hayRectaCandidata:
            elementoDominio.ContEnsayo.eliminarRectaCandidata()
        if elementoDominio.hayPozoCandidato:
            elementoDominio.hayPozoCandidato = False
            elementoDominio.pozoCandidato.hide()
            elementoDominio.pozoCandidato = None

    def setPrevia(self):
        
        if self.label.text() == "Pozo":
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
                if not elementoDominio.hayPozoCandidato:
                    elementoDominio.pozoCandidato = QPushButton(elementoDominio.Dominio)
                    elementoDominio.hayPozoCandidato = True
                elementoDominio.pozoCandidato.setGeometry(QRect(np.int32(self.lineEdit.text()),
                                                                       np.int32(self.lineEdit_2.text()), 25, 20))
                elementoDominio.pozoCandidato.setIcon(QIcon("content/images/redDotIcon.png"))

                
                elementoDominio.pozoCandidato.show()
                 
                

        else:                                   
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.lineEdit_3.text()!= "" and self.lineEdit_4.text() != "":
		
                elementoDominio.ContEnsayo.agregarRectaCandidata(self.cbTipo.currentText(), 
np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()), np.int32(self.lineEdit_3.text()),
                                                                 np.int32(self.lineEdit_4.text()))

    def setPozoExistente(self, idPozo):

        if elementoDominio.Dominio.rectaSeleccionada['id'] == 0:

            coordenadas = elementoDominio.ContEnsayo.retornarCoordenadas(idPozo)
            
            if elementoDominio.pozoSeleccionado == 0:
                self.lineEdit.setText(QString.number(coordenadas['x'], 10))
                self.lineEdit_2.setText(QString.number(coordenadas['y'], 10))                

            self.idElemento = idPozo
            self.tipoElemento = "pozo"
            
            if not self.btnActualizar.isVisible():
                self.btnActualizar.setVisible(True)
                self.btnAceptar.setVisible(False)
                self.btnCancelar.setVisible(False)
                self.btnPrevia.setVisible(False)

                self.lineEdit.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.eliminarPlacebos()

            self.lineEdit_3.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.cbTipo.setVisible(False)


            self.label.setText(QApplication.translate("Form", "Pozo", None, QApplication.UnicodeUTF8))

    def setActualizar(self):
        
        elementoDominio.Dominio.rectaSeleccionada['id'] = 0       
        
        if elementoDominio.pozoSeleccionado != 0:
            for pozo in elementoDominio.Dominio.botones:
                if pozo.id == elementoDominio.pozoSeleccionado:
                    pozo.setIcon(QIcon("content/images/blackDotIcon.png"))

                    for pozo in elementoDominio.Dominio.botones:
                        if pozo.id == elementoDominio.pozoSeleccionado:

                            elementoDominio.ContEnsayo.moverPozo(elementoDominio.pozoSeleccionado, np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()))

                            pozo.move(np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()))
                    
                    elementoDominio.pozoSeleccionado = 0
                    return



        if self.tipoElemento == "pozo":
            
            elementoDominio.ContEnsayo.moverPozo(self.idElemento, np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()))

            for pozo in elementoDominio.Dominio.botones:
                if pozo.id == self.idElemento:
                    pozo.move(np.int32(self.lineEdit.text()), np.int32(self.lineEdit_2.text()))

        if self.tipoElemento == "barrera":
             
            elementoDominio.ContEnsayo.actualizarRectaCoord(self.idElemento, np.int32(self.lineEdit.text()),
                                                       np.int32(self.lineEdit_2.text()),  
np.int32(self.lineEdit_3.text()),np.int32(self.lineEdit_4.text()), self.cbTipo.currentText())
            self.update()
            
    def setRectaExistente(self, idElemento, irRE):

        if elementoDominio.pozoSeleccionado == 0:            
            self.tipoElemento = "barrera"
            self.idElemento = idElemento

            recta = elementoDominio.ContEnsayo.buscarRecta(self.idElemento)

            if irRE == 0:
                self.lineEdit.setText(QString.number(recta.x1, 10))
                self.lineEdit_2.setText(QString.number(recta.y1, 10))
                self.lineEdit_3.setText(QString.number(recta.x2, 10))
                self.lineEdit_4.setText(QString.number(recta.y2, 10))
		 
		if recta.tipo == "Positivo":
		    self.cbTipo.setCurrentIndex(1)
		else:
		    self.cbTipo.setCurrentIndex(0)

            else:
                recta = elementoDominio.ContEnsayo.buscarRecta(irRE)
                
                self.lineEdit.setText(QString.number(recta.x1, 10))
                self.lineEdit_2.setText(QString.number(recta.y1, 10))
                self.lineEdit_3.setText(QString.number(recta.x2, 10))
                self.lineEdit_4.setText(QString.number(recta.y2, 10))

		if recta.tipo == "Positivo":
		    self.cbTipo.setCurrentIndex(1)
		else:
		    self.cbTipo.setCurrentIndex(0)
            

            if not self.btnActualizar.isVisible():
                
                self.btnActualizar.setVisible(True)

                self.btnAceptar.setVisible(False)
                self.btnCancelar.setVisible(False)
                self.btnPrevia.setVisible(False)

                self.lineEdit.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.eliminarPlacebos()

            self.label.setText(QApplication.translate("Form", "Recta", None, QApplication.UnicodeUTF8))            
            self.lineEdit_3.setVisible(True)
            self.lineEdit_4.setVisible(True)
            self.label_5.setVisible(True)
            self.label_4.setVisible(True)
            self.label_3.setVisible(True)
	    self.label_2.setVisible(True)
            self.label.setVisible(True)
            self.cbTipo.setVisible(True)



    def actualizarCoordenadasPozo(self, idPozo):        
        for pozo in elementoDominio.Dominio.botones:
            if pozo.id == idPozo:
	        self.lineEdit.setText(QString.number(pozo.x(), 10))
                self.lineEdit_2.setText(QString.number(pozo.y(), 10))
                elementoDominio.Dominio.rectaSeleccionada['id'] = 0
                self.setPozoExistente(idPozo)

    def ocultarFormulario ( self ):
        #Etiqueta de Tipo 
        self.label.setText(QApplication.translate("Form", "Recta", None, QApplication.UnicodeUTF8))
        self.label.setVisible(False)

        #X1
        self.lineEdit.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit.setVisible(False)

        #Y1
        self.lineEdit_2.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_2.setVisible(False)

        #X2
        self.lineEdit_3.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_3.setVisible(False)

        #Y2
        self.lineEdit_4.setText(QApplication.translate("Form", "", None, QApplication.UnicodeUTF8))
        self.lineEdit_4.setVisible(False)

        #X1
        self.label_2.setVisible(False)


        #Y1
        self.label_3.setVisible(False)

        #X2
        self.label_4.setVisible(False)

        #Y2
        self.label_5.setVisible(False)

        #Combo
        self.cbTipo.setVisible(False)


        #Boton Aceptar
        self.btnAceptar.setVisible(False)
           
        #Boton Cancelar
        self.btnCancelar.setVisible(False)

        #Vista Previa
        self.btnPrevia.setVisible(False)

        #Boton Actualizar
        self.btnActualizar.setVisible(False)


    def eliminarPlacebos(self):
        if elementoDominio.ContEnsayo.hayRectaCandidata():
            elementoDominio.ContEnsayo.eliminarRectaCandidata()

        if elementoDominio.hayPozoCandidato:
            elementoDominio.pozoCandidato.hide()
            elementoDominio.pozoCandidato = None
            elementoDominio.hayPozoCandidato = False
"""

class grafica(QGraphicsView):

	global elementoDominio

	id = 0

	def __init__(self, escena, parent):
		super(grafica, self).__init__(escena, parent)

		self.ScrollHandDrag = 1

		self.init()
	def init(self):
		self.setGeometry(10, 10, 220, 220)
		self.setSceneRect(20, 20, 400, 400)
		self.setAcceptDrops(True)
		#self.setMouseTracking(True) 
		self.setObjectName(_fromUtf8("Dominio"))
		self.presionandoRecta = False
		self.idRecta = 1000
		self.botones = []
		self.bGiratorios = []
		self.rectaSeleccionada = {}
		self.rectaSeleccionada['id'] = 0
 
	#Sobreescribimos dragEnterEvent para pemitir
	#la accion de este evento.
	def dragEnterEvent(self, e):
		print "entra?"
		e.accept()
 

	#Evento que es llamado cuando se suelta un elemento
	#dentro del groupbox
	def dropEvent(self, e):
		print "tira?"
		
		elementoDominio.reloj = False
		#Obtenemos la posicion relativa del lugar en que el
		#elemento es soltado
		position = e.pos()
 
		#Si el elemento no existe creamos uno nuevo, en caso contrario
		#arrastramos el elemento ya existente a una nueva posicion en el
		#dominio.
		if elementoDominio.existe == False:
			if elementoDominio.elementoDominio == 0:        
				#groupBox = QGroupBox("title", None)
				b = boton(QIcon("content/images/blackDotIcon.png"), "", None, "pozo")
				b.id = elementoDominio.ContEnsayo.agregarPozo(position.x(), position.y())
				b.setStyleSheet("border: none")             
				b.setGeometry(QRect(position.x(), position.y(), 24, 24))
				self.botones.append(b)
				proxy = self.scene().addWidget(b);
				#self.scene().addWidget(b)
				

			else:

				r = QLineF(position.x(), position.y(), (position.x() + 30), (position.y() + 30))
				elementoDominio.ContEnsayo.agregarRecta(elementoDominio.gbCoord.cbTipo.currentText(), np.float32(r.x1()), np.float32(r.y1()), np.float32(r.x2()), np.float32(r.y2()))

		else:
			for x in self.botones:
				if x.id == elementoDominio.idElemento:
					x.move(position)
					if x.tooltip == "pozo":
						elementoDominio.ContEnsayo.moverPozo(x.id, position.x(), position.y())
						elementoDominio.gbCoord.actualizarCoordenadasPozo(x.id)


		elementoDominio.transicion = False
		elementoDominio.reloj = False
 

		e.setDropAction(Qt.MoveAction)
		e.accept()

	"""
	#Definicion de la funcion para comenzar a dibujar
	def paintEvent(self, e):
		painter = QPainter()
		painter.begin(self)
		painter.setBrush(QColor(0, 255, 127))        
		painter.setBackground(painter.brush())
		painter.setBackgroundMode(Qt.OpaqueMode)
		self.dibujarRectas(painter)
		painter.end()

	#Funcion de dibujado de lineas    
	def dibujarRectas(self, painter):
		self.rectas = elementoDominio.ContEnsayo.dibujarRecta()
		for x in self.rectas:  
			if len(self.rectaSeleccionada) > 0:
				if self.rectaSeleccionada['id'] == x.id:
					painter.setPen(Qt.red)
					painter.drawLine(QLineF( x.x1, x.y1, x.x2, x.y2 ))
					if x.x1 < x.x2 :                        
						painter.drawLine(QLineF( x.x1, x.y1, x.x3, x.y3))
						painter.drawLine(QLineF( x.x4, x.y4, x.x2, x.y2))
					else:
						painter.drawLine(QLineF( x.x1, x.y1, x.x4, x.y4))
						painter.drawLine(QLineF( x.x3, x.y3, x.x2, x.y2))
				else:
					painter.setPen(Qt.blue)
					painter.drawLine(QLineF( x.x1, x.y1, x.x2, x.y2))
					if x.x1 < x.x2 :
						painter.drawLine(QLineF( x.x1, x.y1, x.x3, x.y3))
						painter.drawLine(QLineF( x.x4, x.y4, x.x2, x.y2))
					else:
						painter.drawLine(QLineF( x.x1, x.y1, x.x4, x.y4))
						painter.drawLine(QLineF( x.x3, x.y3, x.x2, x.y2))
			else:
				painter.setPen(Qt.blue)
				painter.drawLine(QLineF( x.x1, x.y1, x.x2, x.y2))
				if x.x1 < x.x2 :
					painter.drawLine(QLineF( x.x1, x.y1, x.x3, x.y3))
					painter.drawLine(QLineF( x.x4, x.y4, x.x2, x.y2))
				else:
					painter.drawLine(QLineF( x.x1, x.y1, x.x4, x.y4))
					painter.drawLine(QLineF( x.x3, x.y3, x.x2, x.y2))

		if elementoDominio.ContEnsayo.hayRectaCandidata():

			painter.drawLine(elementoDominio.ContEnsayo.rectaCandidata.x1, elementoDominio.ContEnsayo.rectaCandidata.y1, elementoDominio.ContEnsayo.rectaCandidata.x2, elementoDominio.ContEnsayo.rectaCandidata.y2)

			self.update()
		"""
	"""
	def mouseMoveEvent(self, e):

		#Buscamos si las coordenadas actuales estan cerca de algun punto de alguna recta
		lista = elementoDominio.ContEnsayo.buscarPuntoEnRecta(np.float32(e.pos().x()), np.float32(e.pos().y()))
		
		botonGiratorio = boton(QIcon("content/images/redDotIcon.png"), "",  elementoDominio.Dominio, "pozo")
		#QtGui.QPushButton(self)
		#Si hay puntos entonces cambiamos icono del mouse, y mostramos boton. De lo contrario
		#eliminamos el boton mostrado.
		if  len(lista) > 0:
			if lista['eje'] == "x":
				self.setCursor(QCursor(Qt.SizeFDiagCursor))
			else:
				self.setCursor(QCursor(Qt.SizeBDiagCursor))

			#Enviamos identificador a funcion que expresa las coordenadas de manera grafica
			elementoDominio.gbCoord.setRectaExistente(lista['id'], self.rectaSeleccionada['id'])

			botonGiratorio.setGeometry (lista['punto'].x(), lista['punto'].y(), 10, 10)
			self.bGiratorios.append(botonGiratorio)
			botonGiratorio.show()
			self.idRecta = lista['id']

		else:
			if not self.presionandoRecta:
				self.setCursor(QCursor(Qt.ArrowCursor))
			botonGiratorio.hide()
			self.aEliminar = []
			
			for x in self.bGiratorios:                
				x.hide()
				self.aEliminar.append(x)

			for x in self.aEliminar:
				try:
					self.bGiratorios.remove(x)
					break
				except ValueError:
					print "Sobrepaso de rangos, advertencia simple"

	def mousePressEvent(self, e):

		if e.button() == Qt.RightButton:

			elementoDominio.selectedMenuMouse["tipo"] = "recta"
			elementoDominio.selectedMenuMouse["id"] = 0


			if np.int(self.cursor().shape()) == 8:
				elementoDominio.selectedMenuMouse["id"] = elementoDominio.ContEnsayo.buscarPuntoPorQ(e.pos().x(), e.pos().y())

			if np.int(self.cursor().shape()) == 7:
				elementoDominio.selectedMenuMouse["id"] = elementoDominio.ContEnsayo.buscarPuntoPorR(e.pos().x(), e.pos().y())

			if elementoDominio.selectedMenuMouse["id"]  != 0:     
				elementoDominio.menuMouse.move(e.pos())                
				elementoDominio.menuMouse.show()

		else:

			#Si el dominio esta comenzado a ser presionado por un cursor que sea
			#utilizado cuando se trabaja con barreras, entonces se setea el atributo
			#self.presionandoRecta a verdadero.
			if np.int(self.cursor().shape()) == 8 or np.int(self.cursor().shape()) == 7:
				self.presionandoRecta = True
				recta = elementoDominio.ContEnsayo.buscarPuntoEnRecta(e.pos().x(), e.pos().y())

				if len(recta) > 0:
					self.rectaSeleccionada['id'] = recta['id']

					for pozo in elementoDominio.Dominio.botones:
						if pozo.id == elementoDominio.pozoSeleccionado:
							pozo.setIcon(QIcon("content/images/blackDotIcon.png"))
							elementoDominio.pozoSeleccionado = 0

	def mouseReleaseEvent(self, e):
		#Dependiendo del tipo de cursos con el que se este modificando la recta
		#se sabra cual es el punto en la misma que hay que modificar
		if e.button() == Qt.LeftButton:
			if np.int(self.cursor().shape()) == 8:
				self.presionandoRecta = False
				elementoDominio.ContEnsayo.actualizarRecta(self.idRecta, e.pos().x(), e.pos().y(), "Q")
				self.update()
			if np.int(self.cursor().shape()) == 7:
				self.presionandoRecta = False
				elementoDominio.ContEnsayo.actualizarRecta(self.idRecta, e.pos().x(), e.pos().y(), "R")
				self.update()
		"""


class escena(QGraphicsScene):
	def __init__(self):
		super(escena, self).__init__()

	def __init__(self, parent):
		super(escena, self).__init__(parent)


	#Sobreescribimos dragEnterEvent para pemitir
	#la accion de este evento.
	def dragEnterEvent(self, e):
		print "APA ENTRO"
		e.setDropAction(Qt.CopyAction)
		e.accept()

	def dropEvent(self, e):
		print "que pasa ce"
		position = e.pos()
		e.setDropAction(Qt.MoveAction)
		e.accept()

	def dragMoveEvent(self, event):

		event.setDropAction(Qt.CopyAction)
		event.accept()




if __name__ == "__main__":

	elementoDominio.ContEnsayo = controlador.Proyecto()

	app = QApplication(sys.argv)

	MainWindow = QMainWindow()

	MainWindow.setGeometry(80, 40, 800, 500)


	"""
	recta = escena.addRect(QRectF(0, 0, 100, 100))

	pushButton = escena.addWidget(QPushButton())

	vista.setGeometry(10, 10, 350, 350)

	"""


	#Seteo del formulario que contendra todos los widgets del dominio
	frame = QFrame(MainWindow)
	
	frame.setGeometry(QRect(170, 80, 471, 351))
	frame.setCursor(QCursor(Qt.ArrowCursor))
	frame.setFrameShape(QFrame.StyledPanel)
	frame.setFrameShadow(QFrame.Raised)
	frame.setObjectName(_fromUtf8("frame"))
	frame.setEnabled(True)
	frame.setStyleSheet("QFrame{background-color: rgb(40, 255, 40); \n"
						"border: 2px solid green; \n"
						"border-radius: 25px}")
	
	groupBoxDominio = QGroupBox(frame)
	groupBoxDominio.setGeometry(QRect(20, 27, 250, 250))
	groupBoxDominio.setCursor(QCursor(Qt.PointingHandCursor))
	groupBoxDominio.setTitle(QApplication.translate("Form", "Dominio", None, QApplication.UnicodeUTF8))

	groupBoxDominio.setStyleSheet("QGroupBox{background-color: white; \n"
						" border: 2px solid green;}")

	
	groupBox = QGroupBox(frame)
	groupBox.setGeometry(QRect(260, 20, 151, 81))
	groupBox.setCursor(QCursor(Qt.PointingHandCursor))
	groupBox.setTitle(QApplication.translate("Form", "Barra Herramientas", None, QApplication.UnicodeUTF8))

	groupBox.setStyleSheet("QGroupBox{border: 2px solid green} \n"
					"QPushButton{border: 2px solid red;}")

	groupBox.setObjectName(_fromUtf8("groupBox"))

	#Creacion de botones de la barra de herramientas
	pozo = boton(QIcon("content/images/blackDotIcon.png"), "", groupBox, "pozo")
	barrera = boton(QIcon("content/images/blackBarrera.png"), "", groupBox, "barrera")

	barrera.setGeometry(QRect(50, 50, 41, 20))
	barrera.id = 1001
		
	#elementoDominio.gbCoord = gbCoordenadas(frame)
	#elementoDominio.gbCoord.setStyleSheet("QGroupBox{border: 2px solid green} \n"
	#						"QLabel, QPushButton{border: 2px solid red;}")

 

	escena = escena(None)

	vista = grafica(escena, frame)
 


	QGraphicsLineItem(0, 0, 450, 950, None, escena) 


	elementoDominio.Dominio = vista

	vista.show()


	MainWindow.show()

	sys.exit(app.exec_())
	
