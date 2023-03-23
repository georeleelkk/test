_temperature      = 25.0
_acidVoltage      = 2032.44
_neutralVoltage   = 1500.0

voltat7 = 0
vlotat4 = 0

def on_button_pressed_a():
    global vlotat4
    basic.show_string("Cal mode")
    basic.show_string("Ph4")
    vlotat4 = pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global voltat7
    basic.show_string("Cal mode")
    basic.show_string("Ph7")
    voltat7 = pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000
input.on_button_pressed(Button.B, on_button_pressed_b)

def read_PH(voltage,temperature):
    global _acidVoltage
    global _neutralVoltage
    slope     = (7.0-4.0)/((_neutralVoltage-1500.0)/3.0 - (_acidVoltage-1500.0)/3.0)
    intercept = 7.0 - slope*(_neutralVoltage-1500.0)/3.0
    _phValue  = slope*(voltage-1500.0)/3.0+intercept
    
    return Math.round(_phValue)

def on_button_pressed_ab():
    read_PH(pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000, input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)