import websocket
from threading import Thread
import time
import sys
import json
import random
import codecs

from SensoresConjunto import sensoresEnConjunto

#este sensor usa 5V
class sensoresEnConjunto():
    def on_message(ws, message):
        print("*"*20)
        print(message)

    def on_error(ws, error):
        print(error)
        pass

    def on_close(ws):
        print("### closed ###")

    def on_open(ws):
        data={"t":1,"d":{"topic":"prueba"}}
        ws.send(json.dumps(data))

        sensores = {
            "sensor_Distancia" : {
                1 : {
                    "Pin1":14,
                    "Pin2":15
                },
                2 : {
                    "Pin1":2,
                    "Pin2":3
                }
            },
            "sensor_Pir" : {
                3 : {
                    "Pin1":4
                },
                4 : {
                    "Pin1":18
                }
            },
            "sensor_TempHum" : {
               
            },
            "sensor_Led" : {
                
            }
        }

        while True:
            vueltas=0
            vueltas2=0
            vueltas3=0

            if len(sensores["sensor_Distancia"].keys()) > 0:
                for x in sensores["sensor_Distancia"]:
                    pin1=sensores["sensor_Distancia"][x]["Pin1"]
                    pin2=sensores["sensor_Distancia"][x]["Pin2"]

                    pinEntrada={"GPIO_TRIGGER":pin1, "GPIO_ECHO":pin2}

                    sensor=sensoresEnConjunto()
                    valorSensor=sensor.leerDistancia(pinEntrada)

                    data={"t":7,"d":{"topic":"prueba","event":"message","data":[
                        {
                            "sensor_id":x,
                            "distancia":valorSensor
                        }
                        ]}}
                    ws.send(json.dumps(data))

                    tamaDiccio=len(sensores["sensor_Distancia"].keys())
                    vueltas=vueltas+1

                    if vueltas==tamaDiccio:
                        break
                time.sleep(1)


            if len(sensores["sensor_Pir"].keys()) > 0:
                for y in sensores["sensor_Pir"]:
                    pin1=sensores["sensor_Pir"][y]["Pin1"]
                    pinEntrada={"pir":pin1}

                    x=sensoresEnConjunto()
                    valorSensor=x.leerPir(pinEntrada)

                    data={"t":7,"d":{"topic":"prueba","event":"message","data":[
                        {
                            "sensor_id":y,
                            "pir":valorSensor
                        }
                        ]}}
                    ws.send(json.dumps(data))

                    tamaDiccio2=len(sensores["sensor_Pir"].keys())
                    vueltas2=vueltas2+1

                    if vueltas2==tamaDiccio2:
                        break
                time.sleep(1)


            if len(sensores["sensor_TempHum"].keys()) > 0:
                for x in sensores["sensor_TempHum"]:
                    pin1=sensores["sensor_TempHum"][x]["Pin1"]
                    pinEntrada={"Id_sensor":x,"TemperaturaHumedad":pin1}

                    x=sensoresEnConjunto()
                    y=x.sensorHumedad(pinEntrada)

                    z=x.sensorTemp(pinEntrada)

                    data1={"t":7,"d":{"topic":"prueba","event":"message","data":[
                        {
                            "sensor_id":x,
                            "tempHum":y
                        }
                        ]}}
                    ws.send(json.dumps(data1))

                    data2={"t":7,"d":{"topic":"prueba","event":"message","data":[
                        {
                            "sensor_id":x,
                            "distancia":z
                        }
                        ]}}
                    ws.send(json.dumps(data2))

                    tamaDiccio3=len(sensores["sensor_Pir"].keys())
                    vueltas3=vueltas2+1

                    if vueltas3==tamaDiccio3:
                        break
                time.sleep(1)

            time.sleep(5)
                
        time.sleep(1)
            #ws.close()
            #print("Thread terminating...")

        Thread(target=run).start()




    if __name__ == "__main__":
        websocket.enableTrace(True)
        if len(sys.argv) < 2:
            host = "ws://159.65.180.20:3333/ws"
        else:
            host = sys.argv[1]


        
        ws = websocket.WebSocketApp(host,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        
        ws.on_open = on_open
        ws.run_forever()