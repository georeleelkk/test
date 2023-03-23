input.onButtonPressed(Button.A, function () {
    basic.showString("Cal mode")
    basic.showString("Ph4")
    basic.showNumber(3)
    basic.pause(1000)
    basic.showNumber(2)
    basic.pause(1000)
    basic.showNumber(1)
    basic.pause(1000)
    _acidVoltage = pins.analogReadPin(AnalogPin.P0) / 1024 * 5000
    basic.showString("Ph7")
    basic.showNumber(3)
    basic.pause(1000)
    basic.showNumber(2)
    basic.pause(1000)
    basic.showNumber(1)
    basic.pause(1000)
    _neutralVoltage = pins.analogReadPin(AnalogPin.P0) / 1024 * 5000
})
function read_PH (voltage: number, temperature: number) {
    slope = (7 - 4) / ((_neutralVoltage - 1500) / 3 - (_acidVoltage - 1500) / 3)
    intercept = 7 - slope * (_neutralVoltage - 1500) / 3
    _phValue = slope * (voltage - 1500) / 3 + intercept
    return Math.round(_phValue)
}
input.onButtonPressed(Button.B, function () {
    basic.showNumber(read_PH(pins.analogReadPin(AnalogPin.P0) / 1024 * 5000, input.temperature()))
})
let _phValue = 0
let intercept = 0
let slope = 0
let _neutralVoltage = 0
let _acidVoltage = 0
let _temperature = 25
_acidVoltage = 2032.44
_neutralVoltage = 1500
