#from colorama import Fore, Back, Style -- not now
import serial

sensor = serial.Serial('/dev/ttyUSB1', 9600,8, stopbits=1, timeout=1, parity=serial.PARITY_NONE)
print("The programm will read the device at ", sensor.name)

while True:
    pac = sensor.read(10)
    pm10 = (((pac[5] * 256) + pac[4]) / 10)
    pm25 = (((pac[3] * 256) + pac[2]) / 10)
    checksum = (pac[2] + pac[3] + pac[4] + pac[5] + pac[6] + pac[7])
#    if (checksum == pac[8]):
    print("pm10 = ", pm10, "mg/m^3")
    print("pm25 = ", pm25, "mg/m^3")
#        print("checksum ok")
#    else:
#        print("checksum fail")
#        for i in range (0,10):
#            print(hex(pac[i]))
