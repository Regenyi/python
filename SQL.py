
######
# PyCharm stuff
####

cmd + j for live templates list eg +m to if main == __name stuff
cmd + p to see paramters for function



cur.execute(
     sql.SQL("insert into {} values (%s, %s)")
         .format(sql.Identifier('my_table')),
     [10, 20])


@database_common.connection_handler
def simple_insert(cursor, table, columns, values):
    cursor.execute(
        sql.SQL(
            """
            INSERT INTO {0} ({1})
            VALUES ({2})
            """
        ).format(
            sql.Identifier(table),
            sql.SQL(", ").join(map(sql.Identifier, columns)),
            sql.SQL(", ").join(map(sql.Literal, values))
        )
    )
a columns és a values is 1-1 lista, ami stringeket tartalmaz


######
# SQL
#######

SELECT * FROM Customers; -> selects all the columns from the "Customers" table
ORDER BY Country DESC; -> előző táblát rendezi a country field alapján csökkenőben 
ORDER BY Country ASC, CustomerName DESC;
LIMIT [no of rows] OFFSET [row num]


CREATE TABLE groc (id INTEGER PRIMARY KEY, name TEXT, db NUMERIC);
INSERT INTO groc VALUES (1, "cucc", 2);


INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
# If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query


SELECT * FROM Customers
WHERE Country='Mexico'; #ha num akkor a szám pl 1 singel quote nélkül, van fiomtiása <, = IN, LIKE, BETWEEN stb


LIKE Operator					Description:
WHERE CustomerName LIKE 'a%'	Finds any values that starts with "a"
WHERE CustomerName LIKE '%a'	Finds any values that ends with "a"
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%_%'	Finds any values that starts with "a" and are at least 3 characters in length
WHERE CustomerName LIKE 'a%o'	Finds any values that starts with "a" and ends with "o"


#The following SQL statement uses the IS NULL operator to list all persons that have no address:
SELECT LastName, FirstName, Address FROM Persons
WHERE Address IS NULL;


SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='München');  # NOT is van


UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico'; # !!!where nélkül mindent felülir az ContactName oszlopban Juannal! 


DELETE FROM Customers
WHERE CustomerName='Alfreds Futterkiste';


ATTILA: 
1. Deleting questions and related records from SQL database
order matters

2. SQL indentifiers as parameters passed by in a secure way
psycopg2.sql.SQL({0}).format(psycopg2.sql.Identifier())
Don’t try to use this SQL with statements or attributes

3. Uploading and deleting files to/from server
File upload with Flask
Deleting files from hard drive with os module

Sources:
SQL string composition: http://initd.org/psycopg/docs/sql.html
Passing parameters to SQL queries: http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries
Upload: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
Delete: https://www.cyberciti.biz/faq/python-delete-remove-file-if-exists-on-disk/


# 13. http://sqlzoo.net/wiki/SELECT_names
# Find the capital and the name where the capital includes the name of the country.
SELECT capital, name FROM world
WHERE capital LIKE concat('%',name,'%')

#Find the country where the capital is the country plus "City".
SELECT name 
  FROM world
WHERE capital = concat(name, ' City')

#Show the name and the extension where the capital is an extension of name of the country.
SELECT name, REPLACE(capital, name, '') FROM world
WHERE capital LIKE concat(name, '_%') 

#Give the name and the per capita GDP for those countries with a population of at least 200 million.
SELECT name, GDP/population FROM world
WHERE population > 200000000 

# this changes name to d and population to ggg in the list
SELECT name d, population ggg
FROM world
WHERE name IN ('France', 'Germany', 'Italy')

# Round this value to the nearest 1000.
SELECT name, ROUND(GDP/population, -3) 
FROM world
WHERE GDP > 1000000000000

# Show the name and capital where the name and the capital have the same number of characters.
SELECT name, capital
  FROM world
 WHERE LENGTH(name) = LENGTH(capital)

# Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word
SELECT name, capital
FROM world
WHERE LEFT(name,1) = LEFT(capital,1) and capital != name

#Find the country that has all the vowels and no spaces in its name.
SELECT name
   FROM world
WHERE name LIKE '%a%' AND 
name  LIKE '%e%' AND 
name  LIKE '%i%' AND 
name  LIKE '%o%' AND 
name  LIKE '%u%' AND name NOT LIKE '% %'

#8. Show the year, subject, and name of Physics winners for 1980 together with the Chemistry winners for 1984
SELECT * FROM nobel
WHERE (subject = 'Physics' AND yr = 1980) + (subject = 'Chemistry' AND yr = 1984)


