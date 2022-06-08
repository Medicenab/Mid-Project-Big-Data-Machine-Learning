# Docker

**Dockerfile**: La plantilla para crear imagenes de Docker. Allí es donde definimos las instrucciones que se ejecutaran al crear el imagen.

**Docker Image:** La Image es un fichero inmutable que contiene todo el codigo, librerías y dependencias para que se ejecute un contenedor.

**Docker Container:** El contenedor es una instáncia de una aplicación contenerizada en Docker. Diferentemente de máquinas virtuales, los contenedores Docker comparten el sistema operativo.

## Dockerfile

En el Dockerfile debemos definir una série de instrucciones que crearan el imagen. Eso incluye la descarga de las dependencias, copiar los ficheros de código al contenedor y el comando que se debe ejecutar en el contenedor.

## Basic commands

`docker build -t <image_name> .`

`docker run [-i -t -p PORT:PORT] <image_name>`