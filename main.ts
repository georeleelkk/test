let _temperature = 25.0
let _acidVoltage = 2032.44
let _neutralVoltage = 1500.0
let voltat7 = 0
let vlotat4 = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showString("Cal mode")
    basic.showString("Ph4")
    vlotat4 = pins.analogReadPin(AnalogPin.P0) / 1024 * 5000
})
function on_button_pressed_b() {
    
    basic.showString("Cal mode")
    basic.showString("Ph7")
    voltat7 = pins.analogReadPin(AnalogPin.P0) / 1024 * 5000
}

input.onButtonPressed(Button.B, on_button_pressed_b)
function read_PH(voltage: number, temperature: number): number {
    
    
    let slope = (7.0 - 4.0) / ((_neutralVoltage - 1500.0) / 3.0 - (_acidVoltage - 1500.0) / 3.0)
    let intercept = 7.0 - slope * (_neutralVoltage - 1500.0) / 3.0
    let _phValue = slope * (voltage - 1500.0) / 3.0 + intercept
    return Math.round(_phValue)
}

function on_button_pressed_ab() {
    read_PH(pins.analogReadPin(AnalogPin.P0) / 1024 * 5000, input.temperature())
}

input.onButtonPressed(Button.B, on_button_pressed_b)
