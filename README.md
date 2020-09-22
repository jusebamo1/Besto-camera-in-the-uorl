# Readme 

[![N|Solid](https://lh3.googleusercontent.com/proxy/zXOtAsOkQ19Te14LY7MGtUH7OWvK-lIxpb8gcYXCcOiYjmsB4fu9riYahu4ETg4QIy4EctZw84qOJqtqxyGnaZhhjWJG4ZKV8M4QdX8vrKuheufWdQ)](https://www.ros.org/)
# Besto-name-in-the-uorld
![alt text](https://i.imgur.com/tC1oo2n.png)
--------------------------


# Besto-Camera-in-the-uorld
--------------------------
Un servidor de cámara web rápido con sensor habilitado para websocket que se puede usar para crear timelapses. El proyecto contiene un servidor express que se ejecuta en una PC para transmitir imágenes de la cámara del teléfono,además de los datos tomados por los sensores del mismo.


## Cómo funciona
--------------------------------
Un cliente se conecta al servidor de la cámara, la página comienza a transmitir imagenes cada segundo. Cuando el servidor de archivo recibe el evento websocket, extrae la imagen del servidor de la cámara y archiva la imagen para su posterior procesamiento durante un período de tiempo.


#### Requirements
----
- Para llevar a cabo este proyecto debes tener preinstalado:
  - ROS Melodic
  - Python 2.7
  - Android app: ROS All Sensors Driver v0.2.8
   - https://play.google.com/store/apps/details?id=org.ros.android.android_all_sensors_driver&hl=es_419

### Installation
---
> Como primer paso debemos clonar el repositorio: 
` git clone "blablbabla"` 
#### Test Camera
- ` cd camara-ros/ python app.py` 
Alli se ejecutara un codigo que genera un link  (http//:localip:5000) y podras ver en tiempo real lo que toma la camara del telefono.


#### Running Web page
- ` cd ros_flask/python index.py` 
Aqui ya se genera la pagina capaz de obtener los datos de :
* illuminance
* imu
* magnetic_field
