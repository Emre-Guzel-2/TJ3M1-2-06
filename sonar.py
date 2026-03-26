# Emre Guzel
# March 24, 2026
# Sonar program

import time
import board
import digitalio

# setting the pins
trig_pin = digitalio.DigitalInOut(board.GP3)
trig_pin.direction = digitalio.Direction.OUTPUT

echo_pin = digitalio.DigitalInOut(board.GP2)
echo_pin.direction = digitalio.Direction.INPUT

print("Starting Sonar...")

while True:
    # trigger the sensor
    trig_pin.value = False
    time.sleep(0.000002)
    trig_pin.value = True
    time.sleep(0.00001)
    trig_pin.value = False

    # 2. Wait for pulse to START (with timeout)
    # 30ms timeout = ~5 meters distance max
    timeout = time.monotonic() + 0.03 
    pulse_start = time.monotonic_ns()
    
    while echo_pin.value == False:
        pulse_start = time.monotonic_ns()
        if time.monotonic() > timeout:
            break

    # 3. Wait for pulse to END (with timeout)
    timeout = time.monotonic() + 0.03
    pulse_end = time.monotonic_ns()
    
    while echo_pin.value == True:
        pulse_end = time.monotonic_ns()
        if time.monotonic() > timeout:
            break

    # 4. calculate only if didn't time out
    duration_ns = pulse_end - pulse_start
    
    if duration_ns > 0:
        duration_us = duration_ns / 1000
        distance = (duration_us * 0.0343) / 2
        
        # only print if distance is within a realistic range
        if 2 < distance < 400:
            print(f"Distance: {distance:.2f} cm")
        else:
            print("Out of range")
    else:
        print("No pulse detected")

    time.sleep(0.1)
