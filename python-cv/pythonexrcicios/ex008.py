m = float(input('Digite a metragem:'))
km  = m/1000
hm = m/100
dm = m/10
cm = m*100
mm = m*1000

print('esse valor de {}m em quilometros:{}km, hectrometros:{}hm, '
      'em decimetros:{}dm, em centimetros: {}cm, em milimetros:{}mm'.format(m, km, hm, dm, cm, mm))