from SensoresConjunto import sensoresEnConjunto
import time
import datetime
import os

import websocket
from threading import Thread
import sys
import json
import random
import codecs

class Sensores:
    def __init__(self):
        self.sensores = {
            "sensor_Distancia" : {
                1 : {
                    "Pin1":14,
                    "Pin2":15
                }
            },
            "sensor_Pir" : {
            
            },
            "sensor_TempHum" : {
               
            },
            "sensor_Led" : {
                
            }
        }



    def pirMetodo(self):
        for x in self.sensores["sensor_Pir"]:
            pin1=self.sensores["sensor_Pir"][x]["Pin1"]
            pinEntrada={"pir":pin1}
            x=sensoresEnConjunto()
            x.leerMovimiento(pinEntrada)

    def ledMetodo(self):
        for x in self.sensores["sensor_Led"]:
            pin1=self.sensores["sensor_Led"][x]["Pin1"]
            pinEntrada={"Nombre":x,"led":pin1}
            opc2 = input("-> ")
            if opc2 == "1":
                x=sensoresEnConjunto()
                x.ledOn(pinEntrada)
            if opc2 == "2":
                x=sensoresEnConjunto()
                x.ledOff(pinEntrada)


    def distanciaMetodo(self):
        for x in self.sensores["sensor_Distancia"]:
            pin1=self.sensores["sensor_Distancia"][x]["Pin1"]
            pin2=self.sensores["sensor_Distancia"][x]["Pin2"]

            pinEntrada={"GPIO_TRIGGER":pin1, "GPIO_ECHO":pin2}

            x=sensoresEnConjunto()
            x.sensorTemp(pinEntrada)

            x=sensoresEnConjunto()
            x.leerDistancia(pinEntrada)




    def tempHumedadMetodo(self):
        for x in self.sensores["sensor_TempHum"]:
            pin1=self.sensores["sensor_TempHum"][x]["Pin1"]
            pinEntrada={"Id_sensor":x,"TemperaturaHumedad":pin1}

            x=sensoresEnConjunto()
            x.sensorHumedad(pinEntrada)

            x=sensoresEnConjunto()
            x.sensorTemp(pinEntrada)






