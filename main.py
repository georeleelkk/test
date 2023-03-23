voltage = 0

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    global voltage
    voltage = pins.analog_read_pin(AnalogPin.P0) / 1024 * 5000
    basic.show_number(voltage)
loops.every_interval(5000, on_every_interval)
