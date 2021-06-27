# manejo de la fecha y la hora en python
from datetime import datetime

fechaHora = datetime.now()
print(fechaHora)

anio = fechaHora.year
mes = fechaHora.month
dia = fechaHora.day

# horas
hora = fechaHora.hour
minutos = fechaHora.minute
segundos = fechaHora.second
microsegundos = fechaHora.microsecond

print('La hora es  {}:{}:{}'.format(hora,minutos,segundos))
