#!/usr/bin/python
import serial

sensor = serial.Serial('/dev/ttyUSB0', 9600,8, stopbits=1, timeout=1, parity=serial.PARITY_NONE) #Device selection coming soon...
sensor.flushInput()

print("The programm will use the device ", sensor.name)

while True:
    '''
    Msg header - AA.
    Msg tail  -  AB
    Cmd No.   -  C0
    Checksum = sum of data1 to data6
    pm2.5 value = ((data2*256)+data1)/10)
    pm10 value = ((data4*256)+data3)/10)
    data5 & data6 - ID (I'm not planning of using them)
    '''
    pac = sensor.read(10)
    pm10 = (((pac[5] * 256) + pac[4]) / 10)
    pm25 = (((pac[3] * 256) + pac[2]) / 10)
    checksum = (pac[2] + pac[3] + pac[4] + pac[5] + pac[6] + pac[7])
    if (checksum == pac[8]):
        print("pm10 = ", pm10, "mg/m^3")
        print("pm2.5 = ", pm25, "mg/m^3")
        print("checksum ok")
    else:
        print("checksum fail")
        for i in range (0,10):
            print(hex(pac[i]))
            

