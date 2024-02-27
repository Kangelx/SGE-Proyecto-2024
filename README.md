# AlpacApp Incidents
![308286538-19ea4930-cdb6-41e9-ae77-a4d0a5e7b101](https://github.com/Kangelx/SGE-Proyecto-2024/assets/92815915/876698dc-8b9e-41e2-8f8d-aac22cc78f73)


# PROYECTO INTERMODULAR EQUIPO 3:Sistemas de Gestión Empresarial - Programa con Python
## [Página Principal](https://github.com/Kangelx/Proyecto2024-2025/blob/main/README.md)
</head>
  <body>
    <header class="page-header" role="banner">
      <h1 class="project-name">MARKDOWN SGE: PROGRAMA CON PYTHON</h1>
    </header>
   

<h3 id="indice">INDICE</h3>
    <ul>
      <li><a href="#objetivos">OBJETIVOS</a></li>
      <li><a href="#codigo">FUNCIONES Y MÉTODOS</a></li>
      <li><a href="#clases">CLASE INCIDENCIAS</a></li>
      <li><a href="#autores">AUTORES DEL PROYECTO</a></li>
      </ul>
    
    

<div id='objetivos'/>

## Objetivos del proyecto

- El script se conecta a una API para gestionar incidencias. Permite al usuario ver todas las incidencias disponibles, seleccionar una incidencia específica para realizar acciones como marcarla como terminada y calcular el tiempo total dedicado a ella.


<div id='codigo'/>

## Funciones y métodos 
1. hacer_post(url, datos, token, i):
   - Este método hace una solicitud GET a la API para obtener información sobre una incidencia específica con el ID i.
   - **Parámetros:**
     - url: La URL base de la API.
     - datos: Los datos de inicio de sesión (nombre de usuario y contraseña).
     - token: El token de autenticación necesario para acceder a la API.
     - i: El ID de la incidencia que se quiere obtener.
   - **Retorna:**
     - Un objeto JSON con la información de la incidencia.

2. devolverTotal(url, datos, token):
   - Este método hace una solicitud GET a la API para obtener información sobre todas las incidencias disponibles.
   - **Parámetros y retorno:** Similar a hacer_post, pero devuelve información sobre todas las incidencias.

3. Loop para mostrar todas las incidencias:
   - Utiliza la función devolverTotal para obtener información sobre todas las incidencias disponibles.
   - Utiliza un bucle while para mostrar cada incidencia hasta que el contador i sea igual al total de incidencias.

4. Registro y gestión de incidencias:
   - Solicita al usuario que introduzca el ID de una incidencia.
   - Permite al usuario marcar la incidencia como terminada o no terminada.
   - Cronometra el tiempo dedicado a la incidencia y muestra el tiempo total.
   - Guarda la información de la incidencia en un archivo pickle llamado "Incidencias.pickle".


<div id='clases'/>

## Clase Incidencia

- **Atributos:**
  - idIncidencia: El ID de la incidencia.
  - cerrada: Un indicador booleano que indica si la incidencia está cerrada o no.
  - minutos, segundos, horas: El tiempo dedicado a la incidencia en minutos, segundos y horas respectivamente.

- **Descripción:**
  Estos métodos proporcionan una interfaz para acceder y modificar los atributos de una instancia de la clase Incidencia. La clase puede ser utilizada para representar y manejar información relacionada con las incidencias de un sistema.
  
- **Métodos:**
  - `__init__(self, idIncidencia=None, cerrada=None, horas=None, minutos=None, segundos=None):`
    - Constructor de la clase.
    - **Parámetros:**
      - idIncidencia: El ID de la incidencia (opcional, por defecto None).
      - cerrada: El estado de la incidencia (opcional, por defecto None).
      - horas, minutos, segundos: El tiempo dedicado a la incidencia (opcional, por defecto None).
    - Inicializa los atributos de la clase con los valores proporcionados.
    
  - `getIdIncidencia(self) -> int:`
    - Método para obtener el ID de la incidencia.
    - **Retorna:**
      - El ID de la incidencia.
      
  - `getMinutos(self) -> int:`
    - Método para obtener los minutos dedicados a la incidencia.
    - **Retorna:**
      - Los minutos dedicados.
      
  - `getSegundos(self) -> int:`
    - Método para obtener los segundos dedicados a la incidencia.
    - **Retorna:**
      - Los segundos dedicados.
      
  - `getHoras(self) -> int:`
    - Método para obtener las horas dedicadas a la incidencia.
    - **Retorna:**
      - Las horas dedicadas.
      
  - `getCerrada(self) -> bool:`
    - Método para obtener el estado de la incidencia (cerrada o no cerrada).
    - **Retorna:**
      - True si la incidencia está cerrada, False si no lo está.

<div id='autores'/>
  ## **Autores del proyecto**
### *Aplicación móvil*
- :iphone: Diego Corominas Gómez :iphone:
- :llama: Oana Irina Cutitaru Ciobanu :llama:

### *Aplicación de escritorio*
- :headphones: Paula Díaz Santos :headphones:
- :desktop_computer: Ángel García García :desktop_computer:

### *Python*
- :snake: Rubén Cortés Muñoz :snake:

### *Base de datos*
- :file_folder: Pablo Sainz Luque :file_folder:
