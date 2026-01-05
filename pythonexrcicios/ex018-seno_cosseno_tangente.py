from math import radians, sin, cos, tan
angulo = float(input('Valor do angulo:'))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Com o angulo {} temos: \nseno={:.2f} \ncoseno={:.2f} \ntangente={:.2f}'.format(angulo,seno, coseno, tangente))