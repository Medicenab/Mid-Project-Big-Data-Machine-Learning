![](https://api.brandy.run/core/core-logo-wide)

# SQL Basics Exercises

En la carpeta de data en el nivel superior de ese repo encontrarás el fichero `pagila.pgsql`, crea un nuevo database y ejecutalo en pgAdmin. Esa será la base de datos usada en ese ejercício. 

Crea un fichero de texto llamado `solutions.pgsql` y pega en él todas tus soluciones. Acuerdate de poner `;`  al final de cada query y usa comentarios para indicar cual es el ejercicio correspondiente.

## Entity Relations

![](sakila.png)

## SELECT statements

- 1.1 Seleciona todas las columnas de la tabla actor

- 1.2 Seleciona solo last_name de la tabla actor

- 1.3 Seleciona una tabla con las siguientes columnas:

|COLUMN NAME|Note|
|---|---|
|title                 |Exists in film table.|
|description           |Exists in film table.|
|rental_duration       |Exists in film table.|
|rental_rate           |Exists in film table.|
|total_rental_cost     |rental_duration * rental_rate|

## DISTINCT operator

- 2.1 Seleciona todos los apellidos diferentes de la tabla actor

- 2.2 Seleciona todos los codigos postales diferentes de la tabla address

- 2.3 Seleciona todos los ratings diferentes de la tabla film

## WHERE clause

- 3.1 Seleciona `title, description, rating, movie length` de las películas que tienen duración de 3 o más horas

- 3.2 Seleciona `id, amount, payment_date` de los pagos (payments) hechos después de 05/27/2005

- 3.3 Seleciona la primary key, `amount, payment_date` de los pagos hechos en 05/27/2005

- 3.4 Seleciona todas las columnas de la tabla customer para clientes donde los apellidos empiezan con `S` y el nombre termina con `N`.

- 3.5 Seleciona todas los columnas de la tabla customer donde el cliente está inactivo y su nombre termina con `M`.

- 3.6 Seleciona todas las columnas de la tabla category donde el nombre empieza con `C`, `S` o `T`.

## IN operator

- 4.1 Seleciona los telefonos y districto de la tabla `address` para direcciones en `California, England y Taipei`.

- 4.2 Seleciona todas las columnas de la tabla film para peliculas del tipo `G, PG-13 o NC-17`

## ORDER BY clause

- 5.1 Seleciona todas las columnas de la tabla film y ordena por la duración de las películas

- 5.2 Seleciona los diferentes ratings de la tabla film y ordenales descendientemente

- 5.3 Seleciona la fecha de pago y `amount` en la tabla `payment`, enseña los 20 con mayor `amount`


## JOIN

- 6.1 Seleciona `first_name, last_name` de customers y actors uniendo actores y clientes que tengan el mismo apellido.

- 6.2 Seleciona `city name y country name` de las tablas city y country.
