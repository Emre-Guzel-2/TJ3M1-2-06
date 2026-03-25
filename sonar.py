# Emre Guzel
# March 24, 2026
# Sonar program

# setting the module 
import time
import board
import digitalio

# setting the pins
trig_pin = digitalio.DigitalInOut(board.GP3)
trig_pin.direction = digitalio.Direction.OUTPUT

echo_pin = digitalio.DigitalInOut(board.GP2)
echo_pin.direction = digitalio.Direction.INPUT

# setting the loop for claucitons 
while True:
    # Send trigger pulse
    trig_pin.value = False
    time.sleep(0.000002)        # 2 microseconds
    trig_pin.value = True
    time.sleep(0.00001)         # 10 microseconds
    trig_pin.value = False

    # wait for echo to start (with timeout)
    timeout = time.monotonic() + 0.02
    while echo_pin.value == False:
        pulse_start = time.monotonic()
        if time.monotonic() > timeout:
            break

    # wait for echo to end (with timeout)
    timeout = time.monotonic() + 0.02
    while echo_pin.value == True:
        pulse_end = time.monotonic()
        if time.monotonic() > timeout:
            break

    # calculate distance only if both values were captured
    try:
        duration = (pulse_end - pulse_start) * 1_000_000
        distance = (duration * 0.0343) / 2
        print(f"Distance: {distance:.2f} cm")
    except:
        print("No echo detected - check wiring")

    time.sleep(0.1)