# Big Data &  BARCELONA!

Hola!, Bienvendio a mi proyecto de mitad de Bootcamp, en este repositorio encontraras todo para poder visualizar y comprender una base de datos sobre la inmigracion en Barcelona durante los años 2015,2016 y 2017. esta base de datos tiene registrada la inmigracion a esta ciudad dependinendo de los distritos y la nacionalidad de los nuevos residentes. Por lo que la mejor manera de ver estos datos es de forma grafica, ademas de procesar y limpiar los datos usando las herramientas que veras a continuacion. 

## Estructura de las Carpetas
Este proyecto esta dividido en dos carpetas principales `API` y `DASHBOARD`, en las cuales deberas ejecutar en tu propio equipo para poder acceder al Dashboard final, pero su instalacion es muy facil. Primero vamos a ejecutar la carpeta `API`, cuando esta este en linea podremos ejecutar la carpeta `DASHBOARD`.

## Tecnologias
- streamlit
- pandas
- matplotlib
- mongoDB
- Docker
- Heroku

## Ejecutar la API
La funcion de la `API` es hacer peticiones precisas a nuestra dase de datos.Esta base se encuentra en la nube con el servicio de mongoDB. Los archivos que tienes aqui tienen lo necesario para poder acceder a esta informacion. 
Antes que nada debes crear un nuevo entorno de coda, con el siguiente comando en tu terminal. El cual debes crear cuando estes en la carpeta raiz de este proyecto (la que contiene API y DASHBOARD)

`conda create --name nombrequequieras python=3.9`

y accedemos a el con:

`conda activate nombrequequieras`

e instalamos las siguientes librerias, usando el comando `pip install`

-fastapi==0.78.0

-pymongo==4.1.1

-dnspython==2.2.1 


**DOCKER**
Asegurate de instalar DOCKER, que nos permitira crear una computadora virtual esto lo haras con el ejecutable que descargaras de internet 

- [Instalar Docker](https://www.docker.com/products/docker-desktop/)
Ahora toca montar la computadora virtual, en la terminal nos vamos a la carpeta `MID_PROYECT/API` y ejecutamos los siguientes comandos

-`docker build .`

-`docker build -t miapi .`

-` docker run -p 7070:8080 miapi`

listo!, ahora podemos subir nuestra API a la nube, con la seguridad de la maquina virtual. 

**HEROKU**
Ahora toca subir la API a Heroku, por lo que debes hacer una cuenta, e istalarla en la terminal. Nos vamos a `MID_PROYECT/API` y sigues los pasos los veras aqui:
https://api-midproject.herokuapp.com/BCN
- `heroku login`

- `heroku container:login`

- `heroku login`

- `heroku login`

## Ejecutar el DASHBOARD
Ahora que ya tenemos la API lista ahora nos movemos a la carpeta `MID_PROYECT/DASHBOARD`y creamos un entorno nuevo de Conda para ejecutar Streamlit y evitar conflictos con otras librerias. 

`conda create --name streamlit python=3.9`

y accedemos a el con:

`conda activate streamlit`

e instalamos las siguientes librerias, usando el comando `pip install`

-streamlit==1.9.1   

-matplotlib==3.5.2   

Y ahora istalamos Streamlit y  con un comando `pip`

-`pip install streamlit `

-`pip install Matplotlib  `

y por ultimo, ya podemos ejecutar nuestro Dashboard, para poder visualizar la base de datos de Barcelona. Para eso debemos ejecutar este, con el siguente comando:

-` streamlit run main.py `
La terminal nos pasara dos URL, en donde podemos acceder al Dashboard y poder utilizarlo, este funcionana mientras este comando este en ejecucion. 





