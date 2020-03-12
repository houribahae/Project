import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyACM0') # définir le port
analog_input = board.get_pin('a:0:i') # int analog_input = A0
led1 = board.get_pin('d:11:p') # int led1 = 11;"
led2 = board.get_pin('d:13:o') # int led2 = 13;"
#(‘i’ for input, ‘o’ for output, ‘p’ for pwm)


while True: #  ici la procédire loop()
    analog_value = analog_input.read() #analog_value =  analogRead(A0)
    valeur = board.digital[10].read()   #valeur = digitalRead(10)
    if valeur > 50 :
        led2.write(1) #1 <=> digitalWrite(13, HIGH);
        time.sleep(1) # en second delay(1000);   
    else:
        led2.write(0) 
        time.sleep(1)
        
    


