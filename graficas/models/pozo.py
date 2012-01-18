class pozo(object):

        id = 0
        
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.ensayos=[]
                self.observaciones=[]



                
        def agregarObservaciones(self, observaciones):
                self.observaciones.append(observaciones)
        def agregarEnsayo(self, ensayo):
                self.ensayos.append(ensayo)
        def actualizarCoordenadas(self, x, y):
                self.x = x
                self.y = y
               
