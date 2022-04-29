![](https://api.brandy.run/core/core-logo-wide)

# SQL Advanced Exercises

En la carpeta de data en el nivel superior de ese repo encontrarás el fichero `pagila.pgsql`, crea un nuevo database y ejecutalo en pgAdmin. Esa será la base de datos usada en ese ejercício. 

Crea un fichero de texto llamado `solutions.pgsql` y pega en él todas tus soluciones. Acuerdate de poner `;`  al final de cada query y usa comentarios para indicar cual es el ejercicio correspondiente.

## Entity Relations

![](img/sakila.png)


## Write the following queries

- 1. Seleciona las columnas `title, description, length y type`, donde type es una columna que categoriza las películas como `feature, medium, short` segun su duración.
    - short <= 50 min
    - 50 min < medium <= 75 min
    - feature > 75 min

- 2. A partir de los types definidos en la query anterior, calcula la media de duración en cada categoria.

- 3. Seleciona actor_id, first_name, last_name y starred (en cuantas películas estuvo cada actor) para todos los actores.

- 4. Seleciona actor_id y `full_name` (compusto por first_name y last_name), pero solo de los actores que hayan estado en por menos 35 peliculas.

- 5. ¿Cuantas películas ha hecho cada actor de média?

- 6. A partir de las queries anteriores, seleciona solo aquellos actores que estuvieron en menos películas que la média.

- 7. Seleciona todos los customer (first_name y last_name) y todas las películas (title, length y type) que ya hayan alquilado, clasificadas como `short, medium, feature`.

- 8. Seleciona los customer (first_name y last_name) para aquellos customer que en algun momento hayan alquilado una peli del tipo `short`

- 9. 🔥HARD🔥 :  Seleciona los customer (first_name y last_name) para aquellos que hayan alquilado _por lo menos_ 3 películas del tipo `short`.

- 10. Seleciona todos los actores que hayan participado en películas del tipo `short`, pero solo las películas alquiladas por los clientes de la query anterior (#9)
