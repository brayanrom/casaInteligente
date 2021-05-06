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
                }
            },
            "sensor_TempHum" : {
               
            },
            "sensor_Led" : {
                
            }
        }

tamaDiccio=len(sensores["sensor_Distancia"].keys())
print(tamaDiccio)