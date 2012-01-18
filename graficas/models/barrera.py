import numpy as np

class barrera():
                
                id = 0
                        
                def __init__(self, x1, x2, y1, y2, tipo):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.tipo = tipo
                                self.calcularRecta()
      

                def actualizarBarrera(self, x1, x2, y1, y2, tipo):
                                self.x1 = x1
                                self.x2 = x2
                                self.y1 = y1
                                self.y2 = y2
                                self.tipo = tipo
                                self.calcularRecta()

                def calcularRecta( self ):
      
                                self.m  =  (self.y2 - self.y1)  /   (self.x2 - self.x1) 
                                self. n = 0
                                xPorm = self.m * self.x1

                                if xPorm < 0 :
                                                self.n = self.y1 +  xPorm
                                else:
                                                self.n = self.y1 -  xPorm

 
                                self.x3 = self.x1 - 600

                                self.y3 = (self.m * self.x3) + self.n
                                
                                self.x4 = self.x2 + 600
                                
                                self.y4 = (self.m * self.x4) + self.n


