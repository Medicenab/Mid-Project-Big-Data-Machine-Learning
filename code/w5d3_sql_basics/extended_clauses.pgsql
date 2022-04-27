-- SELECT son las queries para leer datos de las bbdd

-- SELECT <columns> FROM <table>

-- Las comillas dobles ( "" ) se utilizan en los nombres de columnas y tablas, nunca en los String
-- Se pueden omitir las comillas dobles salvo en el caso de columnas/tablas cuyo nombre contiene un espacio
-- o es una palabra reservada especial (por ejemplo, una columna llamada Select)
SELECT "name" FROM country;
-- Las queries deben terminar con un punto-coma ( ; ) 

-- Se pueden separar los nombres de columnas por coma ( , )

SELECT "name", continent FROM country;

-- El asterísco ( * ) es el comodín, significa todo
SELECT * FROM country;

select * from country;

SeLeCt NAME, rEGiOn FrOm CounTry;

-- SQL no es case sensitive, salvo en con el uso de comillas

-- En la clausula SELECT, podemos "filtrar" que columnas (atributos) queremos, pero no las filas (registros)
-- La query arriba devuelve todos los name y region para todos los países, i.e.: todas las filas

-- Es posible realizar operaciones entre las columnas. En este caso, estamos dividiendo la poblacion entre
-- el area de la superficie del pais
SELECT population/surfacearea FROM country;


-- Si queremos filtrar las filas, necesitamos de otra clausula: la clausula WHERE

SELECT * FROM country
WHERE "name"='Spain';
-- Las comillas simple ( '' ) siempre designan Strings

-- No importan, en SQL, ni el case, ni los espacios en blanco

SELECT * FROM country WHERE "name"='Spain';

SELECT * FROM 							country 

			WHERE 			"name"='Spain';
			
			
SELECT * FROM country
WHERE continent = 'Europe';

SELECT * FROM country
WHERE population > 100000000;

-- La columna de la condición en el WHERE no tienen por que estar en la clausula SELECT
SELECT "name" FROM country
WHERE population > 100000000;


-- Multiple conditions (Conditional operators: AND, OR, NOT, IN, LIKE, etc.)
-- '<>' es la forma antigua de '!='
SELECT * FROM country
WHERE (population > 100000000) AND continent != 'Asia';

-- ORDER BY
SELECT * FROM country
WHERE (population > 100000000)
ORDER BY continent;

-- ORDER BY multiple columns
SELECT * FROM country
WHERE (population > 100000000)
ORDER BY continent, "name";

-- Reverse Ordering (DESC)
SELECT * FROM country
WHERE (population > 100000000)
ORDER BY continent DESC;

SELECT * FROM country
WHERE (population > 100000000)
ORDER BY continent DESC, "name";

SELECT "name" FROM country
WHERE (population > 100000000)
ORDER BY continent DESC, "name";
-- Las columnas del ORDER BY tampoco necesitan figurar en el SELECT

-- Limitar numero de filas en el output
SELECT "name" FROM country
WHERE (population > 100000000)
ORDER BY continent DESC, "name"
LIMIT 5;

-- Limit with offset
SELECT "name" FROM country
WHERE (population > 100000000)
ORDER BY continent DESC, "name"
LIMIT 5 OFFSET 2; -- Enseñamos 5 despues de saltar las 2 primeras


-- GROUP BY
-- Usamos el group by para agrupar filas que tengan un determinado valor en comun convertiendo multiplas filas
-- en una única
-- Eso requiere que las columnas presentes en la tabla final (SELECT) estén en el GROUP BY o tengan funciones
-- AGREGADORAS.
-- https://www.postgresql.org/docs/current/functions-aggregate.html
SELECT continent FROM country
WHERE (population > 100000000)
GROUP BY continent;

-- Se puede asignar un alias a una columna
SELECT continent, SUM(population) AS total_population FROM country
GROUP BY continent;

SELECT continent, SUM(population) AS total_population, ARRAY_AGG("name") AS countries FROM country
GROUP BY continent;

SELECT continent, SUM(population) AS total_population, COUNT(*) AS num_countries FROM country
GROUP BY continent;


-- Selecting Unique elements
SELECT DISTINCT continent FROM country;