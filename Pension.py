import datetime

class VerificaccionPension():
    today = datetime.datetime.now()
    def __init__(self,d = datetime.datetime.now(), s= 'M', i=0):
        self.dia, self.mes, self.año = [int(x) for x in d.split('/')]
        self.sexo = s
        try:
            self.insalubres = i//4
        except:
            print("Numero de años bajo condiciones insalubres invalido")
        try:
            self.inicio = datetime.datetime(self.año, self.mes, self.dia)
        except:
            print("Fecha no valida")
        assert (self.inicio < self.today)
        assert(self.sexo == 'M' or self.sexo == 'F')
        if(self.insalubres > 5):
            self.insalubres = 5
    def _EsPensionado(self):
        if(self.sexo == 'M')and( (self.today - self.inicio).days) >= 365*(60-self.insalubres):
            print("Es pensionado")
        elif(self.sexo == 'F')and( (self.today - self.inicio).days) >= 365*(55 - self.insalubres):
            print("Es pensionada")
        else:
            print("No es pensionado")