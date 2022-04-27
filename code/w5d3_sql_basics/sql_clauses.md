![](https://api.brandy.run/core/core-logo-wide)

# Select Queries

El tipo de query que más frecuentemente usaremos son las queries del tipo `SELECT`, donde pedimos a la base de datos que nos devuelva la información que queremos.

Esas queries devuelven una `tabla` como resultado.

## Anatomy of a query

```postgresql
SELECT <columns> FROM <table>
WHERE <condition>
GROUP BY <columns>
ORDER BY <columns>
LIMIT <value>;
```

En el bloque de codigo arriba vemos el esqueleto de una query select. A cada parte de la query se llama una `cláusula` (`clause`), que se refieren a una de las palabras claves y son responsables por ejecutar parte de la operación. Podemos pensar en las diferentes cláusulas como los bloques que utilizamos para construír nuestra query. No siempre necesitamos todas, pero sí tenemos que tener en cuenta el orden en que están puestas, pues el resultado puede diferir.

## SELECT clause
```postgresql
SELECT * FROM user;
```
Esa cláusula es el corazón de las queries del tipo select y son esenciales para ellas. Hay dos valores que podemos sustituir, la columna, columnas o valores que queremos que compongan las columnas de la tabla resultante y la tabla originaria (o tablas unidas) desde donde vamos recoger essa información.

## WHERE clause
```postgresql
SELECT * FROM user
WHERE name = "John";
```
La cláusula WHERE es la responsable por filtrar los resultados que se nos devuelve segun algun condicional.

## GROUP BY clause
```postgresql
SELECT * FROM user
GROUP BY last_name;
```
La cláusula GROUP BY transforma nuestra tabla diferentes filas en una única segun la columna que se le pase. Es importante que no haya conflitos, por lo tanto los valores que generen conflito tienen que definirse segun alguna operación.

## ORDER BY clause
```postgresql
SELECT * FROM user
ORDER BY user_id;
```
Esa cláusula reordena los elementos de nuestra tabla segun el parametro que indiquemos. Se puede usar la palabra `DESC` para ordenarlo de modo reverso.

## LIMIT clause 
```postgresql
SELECT * FROM user
LIMIT 4;
```
Si no queremos ver todos los resultados, sino que solo los X primeros, podemos utilizar la cláusula LIMIT.