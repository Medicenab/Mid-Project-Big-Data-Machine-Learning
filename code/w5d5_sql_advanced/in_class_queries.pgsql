-- GROUP BY

SELECT ci.name AS city, MAX(co.name) AS country, ARRAY_AGG(cl.language) AS languages, 
       COUNT(cl.language) AS quantity FROM 
	city AS ci
	JOIN
	country AS co
	ON ci.countrycode = co.code
	JOIN
	countrylanguage AS cl
	ON co.code = cl.countrycode
GROUP BY city;


-- WHERE in GROUP BY

SELECT ci.name AS city, MAX(co.name) AS country, ARRAY_AGG(cl.language) AS languages, 
       COUNT(cl.language) AS quantity FROM 
	city AS ci
	JOIN
	country AS co
	ON ci.countrycode = co.code
	JOIN
	countrylanguage AS cl
	ON co.code = cl.countrycode
WHERE ci.name='Madrid'
GROUP BY city;

-- HAVING in GROUP BY

SELECT ci.name AS city, MAX(co.name) AS country, ARRAY_AGG(cl.language) AS languages, 
       COUNT(cl.language) AS quantity FROM 
	city AS ci
	JOIN
	country AS co
	ON ci.countrycode = co.code
	JOIN
	countrylanguage AS cl
	ON co.code = cl.countrycode
GROUP BY city
HAVING COUNT(cl.language) < 4;


-- if...else

SELECT "name", population,
	CASE
		WHEN population > 10000000 THEN 'enormous'
		WHEN population >  1000000 THEN 'large'
		WHEN population >   500000 THEN 'medium'
		WHEN population >    50000 THEN 'small'
		ELSE 'miniscule'
	END AS "size"
FROM city;

/* "python ternary"
'enormous' if population > 10_000_000 else
'large'    if population >  1_000_000 else
'medium'   if population >    500_000 else
'small'    if population >     50_000 else
'minuscule'
*/



-- Get average

SELECT AVG(population)
FROM city;

-- Result: 352158.842460615154

-- Select cities with pop > avg

SELECT "name", population
FROM city
WHERE population > 352158.842460615154; -- hard-coded

-- Using Sub Query
SELECT "name", population
FROM city
WHERE population > (SELECT AVG(population)
								FROM city);
								
								
-- Creating Table
CREATE TABLE population_average AS
SELECT AVG(population)
FROM city;

SELECT * FROM population_average;

SELECT "name", population
FROM city
WHERE population > (SELECT * FROM population_average);


-- Create temporary table
CREATE TEMPORARY TABLE population_average AS
SELECT AVG(population)
FROM city;


SELECT title, pubdate FROM titles
WHERE pubdate > '1993-12-31';

--Exctract
SELECT title, pubdate FROM titles
WHERE EXTRACT(YEAR FROM pubdate) > 1993;

SELECT title, pubdate, EXTRACT(YEAR FROM pubdate) AS "year" 
FROM titles;

SELECT EXTRACT(DAY FROM pubdate), EXTRACT(MONTH FROM pubdate), EXTRACT(YEAR FROM pubdate), pubdate
FROM titles;

-- Select in Range
SELECT title, pubdate FROM titles
WHERE EXTRACT(YEAR FROM pubdate) >= 1990 AND
	  EXTRACT(YEAR FROM pubdate) <= 1999;
	  
SELECT title, pubdate FROM titles
WHERE EXTRACT(YEAR FROM pubdate) BETWEEN 1990 AND 1999;

SELECT a.au_fname, a.au_lname, t.title, t.type
FROM titles AS "t"
	JOIN titleauthor AS ta
		ON  t.title_id = ta.title_id
	JOIN authors AS "a"
		ON ta.au_id = a.au_id;
		
SELECT CONCAT(a.au_fname, ' ', a.au_lname) AS "name", t.title, t.type
FROM titles AS "t"
	JOIN titleauthor AS ta
		ON  t.title_id = ta.title_id
	JOIN authors AS "a"
		ON ta.au_id = a.au_id;
	
	
-- Create temporary
CREATE TEMPORARY TABLE psy_authors AS
SELECT CONCAT(a.au_fname, ' ', a.au_lname) AS "name", COUNT(*)
FROM titles AS "t"
	JOIN titleauthor AS ta
		ON  t.title_id = ta.title_id
	JOIN authors AS "a"
		ON ta.au_id = a.au_id
WHERE t.type='psychology'
GROUP BY "name";



SELECT CONCAT(a.au_fname, ' ', a.au_lname) AS "name", COUNT(*)
FROM titles AS "t"
	JOIN titleauthor AS ta
		ON  t.title_id = ta.title_id
	JOIN authors AS "a"
		ON ta.au_id = a.au_id
WHERE CONCAT(a.au_fname, ' ', a.au_lname)  IN (SELECT name FROM psy_authors)
GROUP BY "name";



SELECT CONCAT(a.au_fname, ' ', a.au_lname) AS "name", COUNT(*), ARRAY_AGG(t.type) AS genres
FROM titles AS "t"
	JOIN titleauthor AS ta
		ON  t.title_id = ta.title_id
	JOIN authors AS "a"
		ON ta.au_id = a.au_id
GROUP BY "name"
HAVING 'psychology'=ANY(ARRAY_AGG(t.type));


SELECT 'psychology'=ANY(ARRAY_AGG(t.type)) as "HAVING", ARRAY_AGG(t.type)
FROM titles AS t
	JOIN titleauthor AS ta
		ON t.title_id = ta.title_id
	JOIN authors AS a
		ON ta.au_id = a.au_id
GROUP BY a.au_fname, a.au_lname;


-- Case 
SELECT * FROM
	(SELECT title,price,
		CASE
			WHEN price > 15 THEN 'expensive'
			WHEN price >  5 THEN 'cheap'
			WHEN price >= 0 THEN 'very cheap'
			ELSE null
		END AS price_range,
		CASE
			WHEN "type"='psychology' THEN true
			ELSE false
		END AS is_psych
	FROM titles) AS BOOKS
WHERE price_range='cheap' AND is_psych;

SELECT title, a.au_fname, a.au_lname FROM titles AS t
	JOIN titleauthor AS ta
		ON t.title_id=ta.title_id
	JOIN authors AS a
		ON a.au_id = ta.au_id
WHERE (a.au_fname, a.au_lname) IN		(SELECT a.au_fname,  a.au_lname
												FROM titles AS "t"
													JOIN titleauthor AS ta
														ON  t.title_id = ta.title_id
													JOIN authors AS "a"
														ON ta.au_id = a.au_id
												WHERE t.type='psychology'
												GROUP BY a.au_fname,  a.au_lname);

