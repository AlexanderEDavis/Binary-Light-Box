def changes2(difference: number, flag: number):
    global Denary
    Denary += difference
    Display(Denary)
def changes4(difference: number, flag: number):
    global Denary
    Denary += difference
    column4 = flag
    Display(Denary)
def changes128(difference: number, flag: number):
    global Denary
    Denary += difference
    column128 = flag
    Display(Denary)
def Display(number: number):
    serial.write_string("/")
    serial.write_number(number)
def changes256(difference: number, flag: number):
    global Denary
    Denary += difference
    column256 = flag
    Display(Denary)
def changes1(difference: number, flag: number):
    global Denary
    Denary += difference
    column1 = flag
    Display(Denary)
def changes16(difference: number, flag: number):
    global Denary
    Denary += difference
    column16 = flag
    Display(Denary)
def changes32(difference: number, flag: number):
    global Denary
    Denary += difference
    column32 = flag
    Display(Denary)
def changes64(difference: number, flag: number):
    global Denary
    Denary += difference
    column64 = flag
    Display(Denary)
def changes8(difference: number, flag: number):
    global Denary
    Denary += difference
    column8 = flag
    Display(Denary)
Denary = 0
serial.redirect(SerialPin.P0, SerialPin.P16, BaudRate.BAUD_RATE9600)
columns = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Denary = 0
Display(Denary)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 1 and columns[0] == 0:
        changes1(1, 1)
    elif pins.digital_read_pin(DigitalPin.P1) == 0 and columns[0] == 1:
        changes1(-1, 0)
    elif pins.digital_read_pin(DigitalPin.P2) == 1 and columns[1] == 0:
        changes2(2, 1)
    elif pins.digital_read_pin(DigitalPin.P2) == 0 and columns[1] == 1:
        changes2(-2, 0)
    elif pins.digital_read_pin(DigitalPin.P3) == 1 and columns[2] == 0:
        changes4(4, 1)
    elif pins.digital_read_pin(DigitalPin.P3) == 0 and columns[2] == 1:
        changes4(-4, 0)
    elif pins.digital_read_pin(DigitalPin.P4) == 1 and columns[3] == 0:
        changes8(8, 1)
    elif pins.digital_read_pin(DigitalPin.P4) == 0 and columns[3] == 1:
        changes8(-8, 0)
    elif pins.digital_read_pin(DigitalPin.P6) == 1 and columns[4] == 0:
        changes16(16, 1)
    elif pins.digital_read_pin(DigitalPin.P6) == 0 and columns[4] == 1:
        changes16(-16, 0)
    elif pins.digital_read_pin(DigitalPin.P7) == 1 and columns[5] == 0:
        changes32(32, 1)
    elif pins.digital_read_pin(DigitalPin.P7) == 0 and columns[5] == 1:
        changes32(-32, 0)
    elif pins.digital_read_pin(DigitalPin.P8) == 1 and columns[6] == 0:
        changes64(64, 1)
    elif pins.digital_read_pin(DigitalPin.P8) == 0 and columns[6] == 1:
        changes64(-64, 0)
    elif pins.digital_read_pin(DigitalPin.P9) == 1 and columns[7] == 0:
        changes128(128, 1)
    elif pins.digital_read_pin(DigitalPin.P9) == 0 and columns[7] == 1:
        changes128(-128, 0)
    elif pins.digital_read_pin(DigitalPin.P10) == 1 and columns[8] == 0:
        changes256(256, 1)
    elif pins.digital_read_pin(DigitalPin.P10) == 0 and columns[0] == 1:
        changes256(-256, 0)
basic.forever(on_forever)
