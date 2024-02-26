import os
import pickle
import time
import requests
import json

# def hacer_post(url, datos):
#     try:
#
#         respuesta = requests.post(url, json=datos)
#         respuesta.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa (código de estado distinto de 2xx)
#         return respuesta.json()  # Devuelve la respuesta en formato JSON si la solicitud es exitosa
#     except requests.exceptions.RequestException as e:
#         print("Error al hacer la solicitud:", e)
#         return None
#
# url = "http://localhost:4001/login"
# datos = {"username": "m","password": "m"}  # Aquí deberías proporcionar los datos que deseas enviar en el POST
# respuesta = hacer_post(url, datos)
# if respuesta:
#     print("Respuesta recibida:", respuesta)
# else:
#     print("No se pudo obtener respuesta.")

# i=1
# list_names=list()
# try:
#     while True:
#         url='http://localhost:4001/incidencia/{}'.format(i)
#         r=requests.get(url)
#         # j=r.json()
#         # name=j['descripcion']
#         print(r)
#         i+=1
# except KeyError:
#     print()

from Incidencia import Incidencia
horas=0
minutos=0
segundos=0
booleano=False

absFilePath = os.path.abspath(__file__)
Path , filename =os.path.split(absFilePath)
# crea el fichero si no existe
with open("Incidencias.pickle", "ab+") as f:
     pass
while True:
    try:
        print("Id de incidencia")
        id = int(input())
        break
    except ValueError:
        print("El ID debe ser numerico")

print(f"Reparando incidencia {id}")
inicio = time.time()
print("Cerrar incidencia (terminado? si/no)")
terminado=input()
segundos=time.time()-inicio;

if terminado.upper()=="si".upper():
    booleano=True

listaIncidencias=[]
with open("Incidencias.pickle", "rb") as f:
    try:
        while True:
            listaIncidencias.append(pickle.load(f))
    except EOFError:
        pass

Encontrado=False
incidenciaAux=Incidencia()
for v in listaIncidencias:
    if v.getIdIncidencia() == id:
        Encontrado=True
        incidenciaAux=v

if Encontrado==True:
    segundos=segundos+(int(incidenciaAux.getHoras())*3600)+(int(incidenciaAux.getMinutos())*60)+int(incidenciaAux.getSegundos())
    listaIncidencias.remove(incidenciaAux)
    if segundos>=60:
        minutos=segundos/60
        segundos=segundos%60
        if minutos>=60:
            horas=minutos/60
            minutos=minutos%60
    incidencia=Incidencia(id,booleano,int("{:.0f}".format(horas)),int("{:.0f}".format(minutos)),int("{:.0f}".format(segundos)))
    listaIncidencias.append(incidencia)
    print(f"Tiempo total en esta incidencia: {horas:.0f}:{minutos:.0f}:{segundos:.0f}")
else:
    if segundos>=60:
        minutos=segundos/60
        segundos=segundos%60
        if minutos>=60:
            horas=minutos/60
            minutos=minutos%60
    incidencia=Incidencia(id,booleano,int("{:.0f}".format(horas)),int("{:.0f}".format(minutos)),int("{:.0f}".format(segundos)))
    listaIncidencias.append(incidencia)
    print(f"Tiempo total en esta incidencia: {horas:.0f}:{minutos:.0f}:{segundos:.0f}")

# guarda los objetos en un archivo
with open("Incidencias.pickle", "wb") as f:
    for aux in listaIncidencias:
        pickle.dump(aux,f)

f.close()
