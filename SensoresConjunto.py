import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os



class sensoresEnConjunto():
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

    def leerDistancia(self,pinEntrada):
        GPIO_TRIGGER=pinEntrada.get("GPIO_TRIGGER")
        GPIO_ECHO=pinEntrada.get("GPIO_ECHO")

        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

        GPIO.output(GPIO_TRIGGER, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        ditsFinal= round(distance,2)
        #print ("Distancia detectada = "+ditsFinal+ " cm")
        
        return ditsFinal




    def ledOn(self,pinEntrada):
        led=pinEntrada.get("led")
        GPIO.setup(led,GPIO.OUT)    
        GPIO.output(led,1)  

    def ledOff(self,pinEntrada):
        led=pinEntrada.get("led")
        GPIO.setup(led,GPIO.OUT)    
        GPIO.output(led,0)  




    def leerPir(self,pinEntrada):
        pir=pinEntrada.get("pir")
        GPIO.setup(pir, GPIO.IN)     
        deteccionPir=GPIO.input(pir)
        if deteccionPir==0:                
            return 0
        elif deteccionPir==1:               
            return 1




    def sensorHumedad(self,pinEntrada):
        tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        instance = dht11.DHT11(tempHumedadEntrada)
        result = instance.read()
        while True:
            if result.is_valid():
                resultHumed= round(result.humidity,2)
                #print("Humedad: " +str(resultHumed))
                return resultHumed
            else:
                #print("Error en lectura")
                return 0

    def sensorTemp(self,pinEntrada):
        tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        instance = dht11.DHT11(tempHumedadEntrada)
        result = instance.read()
        while True:
            if result.is_valid():
                resultTemp= round(result.temperature,2)
                return resultTemp
            else:
                return 0
