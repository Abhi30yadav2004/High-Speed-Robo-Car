from machine import Pin, PWM
import bluetooth
from ble_uart_peripheral import BLEUART

# Motor control pins
pin1 = Pin(22, Pin.OUT)
pin2 = Pin(21, Pin.OUT)
pin3 = Pin(19, Pin.OUT)
pin4 = Pin(18, Pin.OUT)

# PWM configuration
frequency = 15000

enable = PWM(Pin(23), freq=frequency)
enable1 = PWM(Pin(5), freq=frequency)

# Motor objects
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)
dc_motor1 = DCMotor(pin3, pin4, enable1, 350, 1023)

# Create Bluetooth BLE object
ble = bluetooth.BLE()

# Create BLE UART
uart = BLEUART(ble)


# -----------------------------
# Motor Control Functions
# -----------------------------

def forward():
    dc_motor.forward(100)
    dc_motor1.forward(100)


def backward():
    dc_motor.backwards(100)
    dc_motor1.backwards(100)


def right():
    dc_motor.forward(100)
    dc_motor1.forward(10)


def left():
    dc_motor.forward(10)
    dc_motor1.forward(100)


def stop():
    dc_motor.stop()
    dc_motor1.stop()


# -----------------------------
# Bluetooth Command Handler
# -----------------------------

def on_rx():
    data = uart.read()

    if not data:
        return

    command = data.decode().strip().lower()

    print("UART IN:", command)

    if command == "forward":
        forward()

    elif command == "backward":
        backward()

    elif command == "right":
        right()

    elif command == "left":
        left()

    elif command == "stop":
        stop()

    else:
        print("Unknown command:", command)


# Register Bluetooth interrupt
uart.irq(handler=on_rx)


# Keep the program running
while True:
    pass