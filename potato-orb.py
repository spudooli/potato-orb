import serial
import sys

orbcolor = ""
orbsetcolor = ""

def changeorb( color ):
    global orbsetcolor
    orb.write('G+')
    if color == "blue":
         if color is orbsetcolor:
               print "color is already "+color+" so did nothing"
         else:
               print "Setting orb to "+color
               orb.write('~A 8')
    elif color == "red":
         if color is orbsetcolor:
               print "color is already "+color+" so did nothing"
         else:
               print "Setting orb to "+color
               orb.write('~A  ')
    elif color == "orange":
         if color is orbsetcolor:
               print "color is already "+color+" so did nothing"
         else:
               print "Setting orb to "+color
               orb.write('~A "')
    elif color == "green":
         if color is orbsetcolor:
               print "color is already "+color+" so did nothing"
         else:
               print "Setting orb to "+color
               orb.write('~A ,')
    orbsetcolor = color
    return

orb = serial.Serial(
    port='/dev/ttyS5',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

color = sys.argv[1]
print color
changeorb(color)
