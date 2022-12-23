import os
import time
import datetime
# from io import asyncio
import random
import json
from threading import Thread

from channels.generic.websocket import WebsocketConsumer


class FakeFaroConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        """
        Si el cliente se conecta al socket, una vez aceptada la conexión, se deben
        revisar los archivos existentes dentro del directorio de nubes de puntos,
        se debe armar una lista de tuplas con el siguiente formato:
            [(fecha_modificacion_archivo1, nombre_archivo1), (fecha_modificacion_archivo2, nombre_archivo2), ...]
        """
        
        dir_nube_puntos = r"path\al\directorio\de\las\nubes\de\puntos"
        archivos = ()

        for elemento in os.listdir(dir_nube_puntos):
            if os.path.isfile(os.path.join(dir_nube_puntos, elemento)) and elemento.endswith(".csv"):
                # llenar lista de archivos aca
                pass

        self.send(json.dumps({"batVal": random.randint(), "files": archivos}))
    
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        if "filename" in text_data_json:
            print("nombre archivo a generar: ", filename)

            filename = text_data_json["filename"]

            start_time = time.time()
            # cmd  = r"path\del\archivo\a\ejecutar"
            # t = Thread(target=os.system, args=[cmd,])
            # t.start()

            # while t.isAlive():
            #     pass
            elapsed_time = time.time() - start_time

            """
            De aquí en adelante se debe revisar que el archivo de la nube de puntos
            se haya creado en el escritorio. Se debe revisar la carpeta de nubes de puntos,
            volver a obtener los archivos existentes y enviarlos al cliente a través del socket
            """

            files = []

                
            self.send(json.dumps({"elapsed_time": elapsed_time, "files": files}))
            
        else:
            print("cualquier weaita: ignorar!")
        