from PyQt4 import QtCore, QtGui
from pozo  import pozo
from barrera import barrera
import numpy as np

class Proyecto(object):
    
    def __init__(self):        
        self.ultimoIdEns=0
        self.ultimoIdObs=0
        self.ensayos=[]
        self.observaciones=[]

        #Lista que guardan pozo y recta
	self.listaPozo = []
        self.listaRecta = []

        #Ultima recta y pozo agregados
        self.idP = 0
        self.idR = 0

        #Recta candidata a ser agregada
        self.rectaCandidata = ""
        self.parametros=[]

    #CRUD de pozos
    def agregarPozo(self, x, y):        
        p = pozo(x, y)
        self.idP = self.idP + 1
        p.id = self.idP
        self.listaPozo.append(p)
        return p.id
                

    def moverPozo(self, idElemento, x, y):
        
        for pozo in self.listaPozo:
            if pozo.id == idElemento:
                pozo.actualizarCoordenadas(x, y)
                return

    def buscarPozo(self, idElemento):
        for p in self.listaPozo:
            if p.id == int(idElemento):
                return p
         
    def removerPozo(self, idElemento):            
        for x in self.listaPozo:
            if x.id == idElemento:
                self.listaPozo.remove(x)
    def optimizacioneslistar(self):
        self.optimizaciones = QtCore.QStringList()
        
        self.optimizaciones << "CALIS" << "THEIS"
         
        return self.optimizaciones
    def optimizacioneslistarmenos(self,nolistar):
        self.opt = QtCore.QStringList()
        for x in self.optimizaciones:
            if x != nolistar:
                #print "muestro " + x
                self.opt << x
        
        return self.opt
    def asociarPozoOptimiazion(self,idElemento,metodo):
        for pozo in self.listaPozo:
            if pozo.id == idElemento:
                self.listaPozoOptimiza[idElemento]=metodo
        print "se agrego a la lista de optimizaciones"




    def retornarCoordenadas(self, idElemento):
        listaRetorno = {}
        listaRetorno["x"] = 0
        listaRetorno["y"] = 0

        for pozo in self.listaPozo:
            if pozo.id == idElemento:
                listaRetorno["x"] = pozo.x
                listaRetorno["y"] = pozo.y
                
                return listaRetorno
            
        return listaRetorno
       

    #CRUD de barreras
    def agregarRecta(self, tipo, x1, y1, x2, y2):        
        r = barrera(x1, x2, y1, y2, tipo)
        self.idR = self.idR + 1
        r.id = self.idR

        self.listaRecta.append(r)

    def buscarRecta(self, idElemento):
        for recta in self.listaRecta:
            if recta.id == idElemento:
                return recta

    def dibujarRecta(self):
        return self.listaRecta
            
    def buscarPuntoEnRecta(self, x, y):
        
        for barrera in self.listaRecta:

            recta = QtCore.QLine(barrera.x1, barrera.y1, barrera.x2, barrera.y2)

            puntoP = QtCore.QPoint(x, y)
            puntoQ = QtCore.QPoint(recta.x1(), recta.y1())

            rectay = QtCore.QLine(puntoP, puntoQ)           

            puntoR = QtCore.QPoint(recta.x2(), recta.y2())

            rectaw = QtCore.QLine(puntoP, puntoR)           

            valor1 = np.absolute(recta.dx() /2)
            valor2 = np.absolute(recta.dy() /2)
            
            #Recta proxima a las x
            if  np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):               
                lista = {}
                lista['punto'] = puntoQ

                lista['eje'] = "x"
                lista['id'] = barrera.id
                return lista
            
            #Recta proxima a las y
            if np.absolute(rectaw.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectaw.dy()) < np.absolute((recta.dy() / 2)):
                lista = {}
                lista['punto'] = puntoR
               
                lista['eje'] = "y"
                lista['id'] = barrera.id
                return lista
        lista = {}
        return lista

    def actualizarRecta(self, idRecta, x, y, tipoPunto):
        for barrera in self.listaRecta:
            if barrera.id == idRecta:
                
                if tipoPunto == "R":                    
                    recta = QtCore.QLine(barrera.x1, barrera.y1, x, y)
                    
                    if np.absolute(recta.dy()) > 1 and  np.absolute(recta.dx()) > 1:
                        barrera.actualizarBarrera(barrera.x1, x, barrera.y1, y, barrera.tipo)
                else:                
                    recta = QtCore.QLine(x, y, barrera.x2, barrera.y2)
                    
                    if np.absolute(recta.dx()) > 1 and np.absolute(recta.dy()) > 1:
                       barrera.actualizarBarrera(x, barrera.x2,  y, barrera.y2, barrera.tipo)

    def actualizarRectaCoord(self, idElemento, x1, y1, x2, y2, tipo):
        for recta in self.listaRecta:
            if recta.id == idElemento:
                recta.actualizarBarrera(x1, x2, y1, y2, tipo)
                return

    def buscarPuntoPorQ(self, x, y):
        for Q in self.listaRecta:
            
            recta = QtCore.QLine(Q.x1, Q.y1, Q.x2, Q.y2)

            puntoP = QtCore.QPoint(x, y)

            puntoQ = QtCore.QPoint(recta.x1(), recta.y1())

            rectax = QtCore.QLine(puntoP, puntoQ)   

            #Recta proxima a las x
            if  np.absolute(rectax.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectax.dy()) < np.absolute((recta.dy() / 2)):               

                return Q.id

    def buscarPuntoPorR(self, x, y):
        for R in self.listaRecta:
            
            recta = QtCore.QLine(R.x1, R.y1, R.x2, R.y2)

            puntoP = QtCore.QPoint(x, y)

            puntoR = QtCore.QPoint(recta.x2(), recta.y2())

            rectay = QtCore.QLine(puntoP, puntoR)   

            #Recta proxima a las x
            if  np.absolute(rectay.dx()) < np.absolute(recta.dx() /2) and  np.absolute(rectay.dy()) < np.absolute((recta.dy() / 2)):               
                
                return R.id

    def eliminarRecta(self, idElemento):
        for recta in self.listaRecta:
            if recta.id == idElemento:
                self.listaRecta.remove(recta)

    def agregarRectaCandidata(self, tipo, x1, y1, x2, y2):
        self.rectaCandidata = barrera(x1, x2, y1, y2, tipo)
           
    def hayRectaCandidata(self):

        if self.rectaCandidata:
            return True

        return False

    def eliminarRectaCandidata(self):
        self.rectaCandidata = ""

    def incluirCandidata(self, signo):
        self.idR = self.idR + 1
        self.rectaCandidata.id = self.idR
	self.rectaCandidata.tipo = signo
        self.listaRecta.append(self.rectaCandidata)
        self.rectaCandidata = None
