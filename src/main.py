import machine
import wifi
from coin import coin_callback

ENV_NAME = "devlopment"
wifi.connect()

pin_coin =  machine.Pin(4, machine.Pin.IN)

while True:
    pass


pin_coin.irq(trigger=machine.Pin.IRQ_FALLING, handler=coin_callback)
