import datetime

class VerificaccionPension():
    today = datetime.datetime.now()
    def __init__(self,d = datetime.datetime.now() ):
        self.dia, self.mes, self.año = [int(x) for x in d.split('/')]
        try:
            self.inicio = datetime.datetime(self.año, self.mes, self.dia)
        except:
            print("Fecha no valida")
        assert (self.inicio < self.today)
        
    def _EsPensionado(self):
        if ((self.today - self.inicio).days) >= 365*(60):
            print("Es pensionado")
        else:
            print("No es pensionado")