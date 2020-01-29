import datetime

class VerificaccionPension():
    today = datetime.datetime.now()
    def __init__(self,d = datetime.datetime.now(), s= 'M'):
        self.dia, self.mes, self.año = [int(x) for x in d.split('/')]
        self.sexo = s
        try:
            self.inicio = datetime.datetime(self.año, self.mes, self.dia)
        except:
            print("Fecha no valida")
        assert (self.inicio < self.today)
    def _EsPensionado(self):
       if(self.sexo == 'M')and( (self.today - self.inicio).days) >= 365:
            print("Es pensionado")
        elif(self.sexo == 'F')and( (self.today - self.inicio).days) >= 365:
            print("Es pensionada")
        else:
            print("No es pensionado")