class reloj():
    activo = True

    def change_status(self):
        if self.activo == False:
            self.activo = True
        else:
            self.activo = False
    
    def show_status(self):


reloj_01=reloj()
