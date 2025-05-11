from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(27)
buzzer = Buzzer(17)
lights = TrafficLights(5,6,13)

print("starting program")
while True:
    button.wait_for_press()
    
    lights.green.on()
    sleep(5)
    lights.green.off()
    
    lights.amber.on()
    sleep(2)
    lights.amber.off()
    
    lights.red.on()
    print("ped cross")
    buzzer.beep()
    sleep(7)
    
    lights.off()
    buzzer.off()
    