# -*- coding: utf-8 -*-
#!/usr/bin/python

from datetime import datetime, timedelta
from sys import stdout
from time import sleep

print(' Cronometro regressivo | programador => mmxm')
segundos = int(input('Digite a quantidade de segundos: '))
tempo = timedelta(seconds=segundos)
print('\n')

while (str(tempo) != '0:00:00'):
    stdout.write("\r%s"%tempo)
    stdout.flush()
    tempo = tempo - timedelta(seconds=1)
    sleep(1)

stdout.write("\r0:00:00")
stdout.flush()
input()