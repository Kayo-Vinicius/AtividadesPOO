import datetime
from datetime import datetime

inicioExp = datetime.now()

fimExp = datetime(2022, 8, 26, 23, 30, 10 )

qtdSegundos = fimExp - inicioExp

segundos = int(qtdSegundos.total_seconds())
minutos = int(qtdSegundos.total_seconds() / 60)
horas = int(qtdSegundos.total_seconds() / 3600)

totalSeg = segundos + minutos + horas
print('O experimento durou %s segundos'%totalSeg)