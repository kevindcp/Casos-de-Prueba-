import datetime

class VerificaccionPension():
    today = datetime.datetime.now()
    def __init__(self,d = datetime.datetime.now() ):
        self.dia, self.mes, self.año = [int(x) for x in d.split('/')]
       