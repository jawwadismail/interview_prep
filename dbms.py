
# *************************************DBMS********************************************

1 => SELECT * FROM weather_table ; 

	 SELECT name,id from weather_table; 
	 SELECT name from weather_table where id = 3 and name = 'Pune'; 
	 SELECT count(*);  # selects all the rows for us

2 => INSERT INTO weather_table (id,name) VALUES (5,'London');
	 
3 => DELETE FROM weather_table where id = 10;
	 DELETE FROM weather_table where 1=1; # will wipe out all the database

4 => UPDATE weather_table set name = 'Panipat' where id = 1;
     UPDATE weather_table set name = 'Panipat' # Here everywhere you will have name as panipat very dangerous

5 => CREATE TABLE weather_table1 ();

6 => SELECT * FROM Prices p, Sales s WHERE p.item ==s.products


************************************W3 SCHOOLS *************************************************************

CustomerID	CustomerName		ContactName		Address			City	PostalCode		Country
			
1			Alfreds 			Maria Anders	Obere Str. 57	Berlin	12209			Germany


SELECT * FROM Customers ;
SELECT DISTINCT col1,col2 from Customers ;	# For selecting distinct values
SELECT DISTINCT Country FROM Customers;
SELECT COUNT(DISTINCT Country) FROM Customers;  # It will list the Count of distinct Countries

SELECT * FROM Customers WHERE Country='Mexico';
SELECT * FROM Customers WHERE Country='Germany' AND City='Berlin';
SELECT * FROM Customers WHERE NOT Country='Germany' AND NOT Country='USA';
SELECT * FROM Customers ORDER BY Country DESC;
SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;


