def updateNumber(flag: number, column: number, difference: number):
    global Denary
    Denary += difference
    columns[column] = flag
    Display(Denary)
def Display(number: number):
    serial.write_string("/")
    serial.write_number(number)
Denary = 0
columns: List[number] = []
serial.redirect(SerialPin.P0, SerialPin.P16, BaudRate.BAUD_RATE9600)
columns = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Denary = 0
Display(Denary)
ready = True

def on_forever():
    if ready:
        if pins.digital_read_pin(DigitalPin.P1) == 1 and columns[0] == 0:
            updateNumber(1, 0, 1)
        elif pins.digital_read_pin(DigitalPin.P1) == 0 and columns[0] == 1:
            updateNumber(0, 0, -1)
        elif pins.digital_read_pin(DigitalPin.P2) == 1 and columns[1] == 0:
            updateNumber(1, 1, 2)
        elif pins.digital_read_pin(DigitalPin.P2) == 0 and columns[1] == 1:
            updateNumber(0, 1, -2)
        elif pins.digital_read_pin(DigitalPin.P3) == 1 and columns[2] == 0:
            updateNumber(1, 2, 4)
        elif pins.digital_read_pin(DigitalPin.P3) == 0 and columns[2] == 1:
            updateNumber(0, 2, -4)
        elif pins.digital_read_pin(DigitalPin.P4) == 1 and columns[3] == 0:
            updateNumber(1, 3, 8)
        elif pins.digital_read_pin(DigitalPin.P4) == 0 and columns[3] == 1:
            updateNumber(0, 3, -8)
        elif pins.digital_read_pin(DigitalPin.P6) == 1 and columns[4] == 0:
            updateNumber(1, 4, 16)
        elif pins.digital_read_pin(DigitalPin.P6) == 0 and columns[4] == 1:
            updateNumber(0, 4, -16)
        elif pins.digital_read_pin(DigitalPin.P7) == 1 and columns[5] == 0:
            updateNumber(1, 5, 32)
        elif pins.digital_read_pin(DigitalPin.P7) == 0 and columns[5] == 1:
            updateNumber(0, 5, -32)
        elif pins.digital_read_pin(DigitalPin.P8) == 1 and columns[6] == 0:
            updateNumber(1, 6, 64)
        elif pins.digital_read_pin(DigitalPin.P8) == 0 and columns[6] == 1:
            updateNumber(0, 6, -64)
        elif pins.digital_read_pin(DigitalPin.P9) == 1 and columns[7] == 0:
            updateNumber(1, 7, 128)
        elif pins.digital_read_pin(DigitalPin.P9) == 0 and columns[7] == 1:
            updateNumber(0, 7, -128)
        elif pins.digital_read_pin(DigitalPin.P10) == 1 and columns[8] == 0:
            updateNumber(1, 8, 256)
        elif pins.digital_read_pin(DigitalPin.P10) == 0 and columns[8] == 1:
            updateNumber(0, 8, -256)
basic.forever(on_forever)
