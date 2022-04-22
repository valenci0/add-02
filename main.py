from machine import ADC
from time import sleep
adc = ADC (27)

val1 = 0
s1 = ADC(27)
convert = 3.3/(65535)

while 1:
    val1 = s1.read_u16()* convert
    res = val1 / 0.01
    reformateado = "{:.2f}".format(res)
    print("la temperatura es:{}".format(reformateado))
    sleep(.5)