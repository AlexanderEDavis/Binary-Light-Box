function updateNumber () {
    Denary = 0
    for (let item = 0; item <= columns.length - 1; item++) {
        if (columns[item]) {
            Denary += columnValues[item]
        }
    }
    updateDisplay(Denary)
}
function updateColumn () {
    for (let item2 = 0; item2 <= columns.length - 1; item2++) {
        updateFlag(item2, sensePins[item2])
    }
}
function switchSensors () {
    if (pins.digitalReadPin(DigitalPin.P1) == 1) {
        sensePins[0] = true
    } else if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        sensePins[0] = false
    }
    if (pins.digitalReadPin(DigitalPin.P2) == 1) {
        sensePins[1] = true
    } else if (pins.digitalReadPin(DigitalPin.P2) == 0) {
        sensePins[1] = false
    }
    if (pins.digitalReadPin(DigitalPin.P3) == 1) {
        sensePins[2] = true
    } else if (pins.digitalReadPin(DigitalPin.P3) == 0) {
        sensePins[2] = false
    }
    if (pins.digitalReadPin(DigitalPin.P4) == 1) {
        sensePins[3] = true
    } else if (pins.digitalReadPin(DigitalPin.P4) == 0) {
        sensePins[3] = false
    }
    if (pins.digitalReadPin(DigitalPin.P6) == 1) {
        sensePins[4] = true
    } else if (pins.digitalReadPin(DigitalPin.P6) == 0) {
        sensePins[4] = false
    }
    if (pins.digitalReadPin(DigitalPin.P7) == 1) {
        sensePins[5] = true
    } else if (pins.digitalReadPin(DigitalPin.P7) == 0) {
        sensePins[5] = false
    }
    if (pins.digitalReadPin(DigitalPin.P8) == 1) {
        sensePins[6] = true
    } else if (pins.digitalReadPin(DigitalPin.P8) == 0) {
        sensePins[6] = false
    }
    if (pins.digitalReadPin(DigitalPin.P9) == 1) {
        sensePins[7] = true
    } else if (pins.digitalReadPin(DigitalPin.P9) == 0) {
        sensePins[7] = false
    }
    if (pins.digitalReadPin(DigitalPin.P10) == 1) {
        sensePins[8] = true
    } else if (pins.digitalReadPin(DigitalPin.P10) == 0) {
        sensePins[8] = false
    }
}
function updateFlag (column: number, flag: boolean) {
    if (flag) {
        columns[column] = true
    } else if (!(flag)) {
        columns[column] = false
    }
}
function updateDisplay (number: number) {
    serial.writeString("/")
    serial.writeNumber(number)
}
let Denary = 0
let columnValues: number[] = []
let columns: boolean[] = []
let sensePins: boolean[] = []
serial.redirect(
SerialPin.P0,
SerialPin.P16,
BaudRate.BaudRate9600
)
sensePins = [false, false, false, false, false, false, false, false, false]
columns = [false, false, false, false, false, false, false, false, false]
columnValues = [1, 2, 4, 8, 16, 32, 64, 128, 256]
Denary = 0
updateDisplay(Denary)
let ready = true
basic.forever(function () {
    if (ready) {
        switchSensors()
        updateColumn()
        updateNumber()
    }
})
