import serial
from time import sleep
prusaPort="Original Prusa i3 MK3"
ender3Port="USB-SERIAL CH340"

def findPort(portName):
    # Find first available Ender3 by searching USB ports.
    # Return serial port object.
    try:
        from serial.tools.list_ports import comports
    except ImportError:
        return None
    if comports:
        com_ports_list = list(comports())
        ender3_port = None
        for port in com_ports_list:
            if port[1].startswith(portName):
                ender3_port = port[0]  # Success; found by name match.
                break  # stop searching-- we are done.
        return ender3_port 

def serialPrint(portName, filepath):
    try:
        import serial.tools.list_ports
    except ImportError:
        return None
    printerPort=findPort(portName)
    ser = serial.Serial(port = printerPort, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    print("port opened")
    sleep(3)

    gcodefile=open(filepath,"r")
    gcode=gcodefile.read().splitlines()
    
    for i,command in enumerate(gcode):
        command=command.split(";")[0]
        gcode[i]=command
    gcode = list(filter(lambda val: val !=  '', gcode))
    length=len(gcode)
    for i,command in enumerate(gcode):
        ser.write((command+"\r\n").encode('ascii'))
        print('command: ' + command)
        print('status: ' + str(i/length*100) + "%")
        while True:
            line=ser.readline()
            print('reading: '+str(line))
            if line == b'ok\n':
                break
    sleep(1)
    ser.close()
    print("port closed")

serialPrint(ender3Port, r"C:\Users\colin\Desktop\PI3_xyzCalibration_cube_0h11m.gcode")

# =============================================================================
# ser = serial.Serial(port = findPort(prusaPort), baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
# sleep(5)
# ser.write(("G28\r\n").encode("ascii"))
# line=b'start\n'
# while line!=b'':
#     line=ser.readline()
#     print('reading '+str(line))
# sleep(1)
# ser.close()
# =============================================================================

