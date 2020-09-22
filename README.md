# Readme 

[![N|Solid](https://lh3.googleusercontent.com/proxy/zXOtAsOkQ19Te14LY7MGtUH7OWvK-lIxpb8gcYXCcOiYjmsB4fu9riYahu4ETg4QIy4EctZw84qOJqtqxyGnaZhhjWJG4ZKV8M4QdX8vrKuheufWdQ)](https://nodesource.com/products/nsolid)


# Besto-camera-in-the-uorld
--------------------------
Un servidor de cámara web rápido con sensor habilitado para websocket que se puede usar para crear timelapses. El proyecto contiene un servidor express que se ejecuta en una PC para capturar imágenes de la cámara del teléfono, además de los datos tomados por los sensores del mismo.
- *Para llevar a cabo este proyecto debes tener preinstalado:*
  - Una versión de ROS
  - Una versión de Python 2.7 o superior
  - Android app: ROS All Sensors Driver v0.2.8

## Cómo funciona
--------------------------------
Simplemente, cuando un cliente se conecta al servidor de la cámara, la página comienza a tomar una foto cada 5 segundos. Cuando el servidor de archivo recibe el evento websocket, extrae la imagen del servidor de la cámara y archiva la imagen para su posterior procesamiento durante un período de tiempo.

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)

# Example 
Este es un ejemplo de cómo se ve la página:
https://drive.google.com/file/d/1pImyNdYkW90UULKF-Dla7w2UJo43IUVZ/view

### Installation
---
Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.
#### Test Camera
- 
##### Running Web page
- 

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
