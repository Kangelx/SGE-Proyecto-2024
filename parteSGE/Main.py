import os
import pickle
import time
import requests
from Incidencia import Incidencia

horas=0
minutos=0
segundos=0
booleano=False
# este metodo verifica que se hayan introducido las credenciales correctamente y devuelve
# en formato json toda la informacion de la incidencia con ID pasado por parameto.
def hacer_post(url, datos, token,i):
    headers = {"Authorization": "Bearer " + token}
    try:
        respuesta= requests.get("http://localhost:4001/incidencia/{}".format(i),json=datos,headers=headers)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None

# metodo que verifica que se hayan introducido las credenciales correctamente
# y devuelve en formato json toda la informacion de todas las incidencias.
def devolverTotal(url, datos, token):
    headers = {"Authorization": "Bearer " + token}
    try:
        respuesta= requests.get("http://localhost:4001/incidencia",json=datos,headers=headers)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None

# contiene el enlace de la pagina de login de la API.
url = "http://localhost:4001/login"
# contiene el nombre de usuario y la contraseña para iniciar sesion
datos = {"username": "m","password": "m"}  # Credenciales del encargado
# contiene el token necesario para acceder a la API.
token = "eyJhbGciOiJIUzUxMiJ9.eyJyb2xlcyI6WyJhZG1pbmlzdHJhZG9yIl0sInN1YiI6Im0iLCJpYXQiOjE3MDg3MTQwODAsImV4cCI6MTcwOTcxNDA4MH0.3nIZEm-VzzfO2kZo05v5LyGB5jYqO2W5HQPVlp3F0FIdRvc29c5dZX3p1_4dEh9rb4EwVkyPWcd1TytRBNiS0g"

# muestra todas las incidencias
i=1
Total=len(devolverTotal(url,datos,token))
while i!=Total:
    respuesta = hacer_post(url, datos,token,i)
    i+=1
    if respuesta:
        print("Respuesta recibida:", respuesta)
    else:
        Total+=1

# abre el fichero, si no existe lo crea en el directorio de trabajo.
absFilePath = os.path.abspath(__file__)
Path , filename =os.path.split(absFilePath)
with open("Incidencias.pickle", "ab+") as f:
     pass

# pide el ID de una incidencia, si la incidencia no existe escribe un mensaje y termina el programa
# controla que solo puedan introducirse numeros.
while True:
    try:
        print("Id de incidencia")
        id = int(input())
        break
    except ValueError:
        print("El ID debe ser numerico")

respuesta = hacer_post(url, datos,token,id)
if respuesta:
    # empieza a cronometrar el tiempo en la incidencia.
    print(f"Reparando incidencia {id}")
    inicio = time.time()

    # Termina de cronometrar el tiempo en la incidencia
    # controla que solo se pueda escribir "si" o "no".
    while True:
        try:
            print("Cerrar incidencia (terminado? si/no)")

            terminado=input()
            if terminado.upper()=="si".upper() or terminado.upper()=="no".upper():
                break
        except ValueError:
            pass

    segundos=time.time()-inicio;
    if terminado.upper()=="si".upper():
            booleano=True

    # abre el fichero y carga todas las incidencias en una lista.
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

    # si la incidencia existe suma el tiempo de esta sesion al escrito en el fichero y lo actualiza
    # si la incidencia no existe se registra una incidencia nueva en el fichero.
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
else:
    print("la incidencia no existe")
