let voltage = 0
basic.forever(function on_forever() {
    
})
loops.everyInterval(5000, function on_every_interval() {
    
    voltage = pins.analogReadPin(AnalogPin.P0) / 1024 * 5000
    basic.showNumber(voltage)
})
