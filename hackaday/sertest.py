import serial
ser = serial.Serial('COM5')  # open serial port
print(ser.name)         # check which port was really used
#ser.timeout =0
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = 8
ser.parity = serial.PARITY_NONE
ser.rtscts = 0
ser.dsrdtr = 1
#ser.write(b'hello')     # write a string
s = ser.read(100)
print(s.decode('utf-8'))
ser.close()             # close port
