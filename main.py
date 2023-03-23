def on_button_pressed_ab():
    read_PH(pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000,
        input.temperature())

def on_button_pressed_a():
    global _acidVoltage, _neutralVoltage
    basic.show_string("Cal mode")
    basic.show_string("Ph4")
    basic.show_number(3)
    basic.pause(1000)
    basic.show_number(2)
    basic.pause(1000)
    basic.show_number(1)
    basic.pause(1000)
    _acidVoltage = pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000
    basic.show_string("Ph7")
    basic.show_number(3)
    basic.pause(1000)
    basic.show_number(2)
    basic.pause(1000)
    basic.show_number(1)
    basic.pause(1000)
    _neutralVoltage = pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000
input.on_button_pressed(Button.A, on_button_pressed_a)

def read_PH(voltage: number, temperature: number):
    global slope, intercept, _phValue
    slope = (7 - 4) / ((_neutralVoltage - 1500) / 3 - (_acidVoltage - 1500) / 3)
    intercept = 7 - slope * (_neutralVoltage - 1500) / 3
    _phValue = slope * (voltage - 1500) / 3 + intercept
    return Math.round(_phValue)
_phValue = 0
intercept = 0
slope = 0

_temperature = 25
_acidVoltage = 2032.44
_neutralVoltage = 1500