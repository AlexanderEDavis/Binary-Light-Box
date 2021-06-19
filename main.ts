function updateNumber (flag: number, column: number, difference: number) {
    Denary += difference
    columns[column] = flag
    Display(Denary)
}
function Display (number: number) {
    serial.writeString("/")
    serial.writeNumber(number)
}
let Denary = 0
let columns: number[] = []
let ready = false
serial.redirect(
SerialPin.P0,
SerialPin.P16,
BaudRate.BaudRate9600
)
columns = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Denary = 0
Display(Denary)
ready = true
basic.forever(function () {
    if (ready) {
        if (pins.digitalReadPin(DigitalPin.P1) == 1 && columns[0] == 0) {
            updateNumber(1, 0, 1)
        } else if (pins.digitalReadPin(DigitalPin.P1) == 0 && columns[0] == 1) {
            updateNumber(0, 0, -1)
        } else if (pins.digitalReadPin(DigitalPin.P2) == 1 && columns[1] == 0) {
            updateNumber(1, 1, 2)
        } else if (pins.digitalReadPin(DigitalPin.P2) == 0 && columns[1] == 1) {
            updateNumber(0, 1, -2)
        } else if (pins.digitalReadPin(DigitalPin.P3) == 1 && columns[2] == 0) {
            updateNumber(1, 2, 4)
        } else if (pins.digitalReadPin(DigitalPin.P3) == 0 && columns[2] == 1) {
            updateNumber(0, 2, -4)
        } else if (pins.digitalReadPin(DigitalPin.P4) == 1 && columns[3] == 0) {
            updateNumber(1, 3, 8)
        } else if (pins.digitalReadPin(DigitalPin.P4) == 0 && columns[3] == 1) {
            updateNumber(0, 3, -8)
        } else if (pins.digitalReadPin(DigitalPin.P6) == 1 && columns[4] == 0) {
            updateNumber(1, 4, 16)
        } else if (pins.digitalReadPin(DigitalPin.P6) == 0 && columns[4] == 1) {
            updateNumber(0, 4, -16)
        } else if (pins.digitalReadPin(DigitalPin.P7) == 1 && columns[5] == 0) {
            updateNumber(1, 5, 32)
        } else if (pins.digitalReadPin(DigitalPin.P7) == 0 && columns[5] == 1) {
            updateNumber(0, 5, -32)
        } else if (pins.digitalReadPin(DigitalPin.P8) == 1 && columns[6] == 0) {
            updateNumber(1, 6, 64)
        } else if (pins.digitalReadPin(DigitalPin.P8) == 0 && columns[6] == 1) {
            updateNumber(0, 6, -64)
        } else if (pins.digitalReadPin(DigitalPin.P9) == 1 && columns[7] == 0) {
            updateNumber(1, 7, 128)
        } else if (pins.digitalReadPin(DigitalPin.P9) == 0 && columns[7] == 1) {
            updateNumber(0, 7, -128)
        } else if (pins.digitalReadPin(DigitalPin.P10) == 1 && columns[8] == 0) {
            updateNumber(1, 8, 256)
        } else if (pins.digitalReadPin(DigitalPin.P10) == 0 && columns[8] == 1) {
            updateNumber(0, 8, -256)
        }
    }
})
