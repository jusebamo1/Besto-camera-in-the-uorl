# Readme 

[![N|Solid](https://lh3.googleusercontent.com/proxy/zXOtAsOkQ19Te14LY7MGtUH7OWvK-lIxpb8gcYXCcOiYjmsB4fu9riYahu4ETg4QIy4EctZw84qOJqtqxyGnaZhhjWJG4ZKV8M4QdX8vrKuheufWdQ)](https://nodesource.com/products/nsolid)


# Besto-camera-in-the-uorld
--------------------------
Un servidor de cámara web rápido con sensor habilitado para websocket que se puede usar para crear timelapses. El proyecto contiene un servidor express que se ejecuta en una PC para capturar imágenes de la cámara del teléfono, además de los datos tomados por los sensores del teléfono.
- *Para llevar a cabo este proyecto debes tener preinstalado:*
  - Tener instalado una versión de ROS
  - Contar con una versión de Python 2.7 o superior
  - Android app: ROS All Sensors Driver v0.2.8

## How it works
--------------------------------
Simply, when a client connects to the camera's server, the page starts taking a picture every 5 seconds. When the archive server receives the websocket event, it pulls the image from the camera server and archives the image for further processing over a period of time.

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)

# Example 
This is an example of what the page looks like:
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
