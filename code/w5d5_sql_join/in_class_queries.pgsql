--UPDATE country
--SET headofstate='Felipe VI';

SELECT "name", headofstate FROM country;

UPDATE country
SET headofstate='Felipe VI'
WHERE "name"='Spain';


SELECT * FROM country
WHERE code='YUG';

-- DELETE
-- https://www.youtube.com/watch?v=i_cVJgIz_Cs

DELETE FROM country CASCADE
WHERE code='YUG';


-- INSERT

INSERT INTO country
VALUES ('SRB', 'Serbia', 'Europe', 'Eastern Europe', 88361, 1992, 6926705, 76, 42168.00, 49677.00, 
	    	'Srbija', 'Republic', '	Aleksandar Vučić', 4080, 'RS');
			
-- DEFAULT, NULL

SELECT "id" FROM city
ORDER BY "id" DESC
LIMIT 1;

INSERT INTO city ("id", countrycode, district, population, "name")
VALUES (4080, 'SBR', 'Belgrade', 1160000, 'Belgrade');

SELECT * FROM country
WHERE "name"='Serbia';


-- JOIN

DELETE FROM city
WHERE countrycode='GBR';

SELECT * FROM 
city AS ci        FULL OUTER JOIN        country AS co
ON ci.countrycode = co.code
WHERE code='GBR';

SELECT * FROM country
WHERE code='GBR';

SELECT ci.name, co.name, (ci.population/co.population) * 100 AS "ratio(%)" FROM 
city AS ci JOIN country AS co
ON ci.population > co.population
WHERE ci.name='Madrid' AND co.population>0;