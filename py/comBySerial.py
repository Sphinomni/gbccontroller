import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600)

while(1):
	ser.write(b"2")
	print time.ctime()
	
	time.sleep(0.2)
	
	ser.write(b"2")

	time.sleep(0.8)