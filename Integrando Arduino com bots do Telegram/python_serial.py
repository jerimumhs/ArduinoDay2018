from serial import Serial

serial_port = '/dev/ttyUSB0'

boud_rate = 9600

conn = Serial(serial_port, boud_rate)

def light_on():
    conn.write(b'1')

def light_off():
    conn.write(b'0')
