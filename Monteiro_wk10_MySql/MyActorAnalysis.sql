USE sakila;

# 1a. Display the first and last names of all actors from the table actor.
#____________________________________________________________________________________________________  1 of 29 EX  ____

SELECT first_name, last_name
FROM sakila.actor;


# 1b. Display the first and last name of each actor in a single column in upper case letters. 
#     Name the column Actor Name.
#____________________________________________________________________________________________________  2 of 29 EX  ____

SELECT concat(first_name, ' ', last_name)
AS Actor_Name
FROM sakila.actor;


# 2a. You need to find the ID number, first name, and last name of an actor, 
#     of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
#___________________________________________________________________________________________________  3 of 29 EX  ____

SELECT actor_id, first_name, last_name
FROM sakila.actor
Where first_name = "Joe";


# 2b. Find all actors whose last name contain the letters GEN:
#___________________________________________________________________________________________________  4 of 29 EX  ____

SELECT first_name as 'First', last_name as 'Last'
FROM sakila.actor
Where last_name LIKE '%gen%';


# 2c. Find all actors whose last names contain the letters LI. This time, 
#     order the rows by last name and first name, in that order:
#__________________________________________________________________________________________________  5 of 29 EX  ____

SELECT first_name as 'First', last_name as 'Last'
FROM sakila.actor
Where last_name LIKE '%LI%'
Order By last_name, first_name;



# 2d. Using IN, display the country_id and country columns of the following countries: 
#     Afghanistan, Bangladesh, and China:
#____________________________________________________________________________________________________  6 of 29 EX  ____

SELECT country_id as 'ID', country as 'Country'
FROM sakila.country
WHERE country 
IN ('Afghanistan', 'Bangladesh', 'China');



# 3a. You want to keep a description of each actor. You don't think you will be performing 
#     queries on a description, so create a column in the table actor named description and 
#     use the data type BLOB (Make sure to research the type BLOB, as the difference between 
#     it and VARCHAR are significant).
#___________________________________________________________________________________________________  7 of 29 EX  ____

USE sakila;
ALTER TABLE sakila.actor 
ADD description BLOB;

SELECT * FROM sakila.actor;



# 3b. Very quickly you realize that entering descriptions for each actor is too much effort. 
#     Delete the description column.
#__________________________________________________________________________________________________  8 of 29 EX  ____

ALTER TABLE sakila.actor 
Drop description;

SELECT * FROM sakila.actor;



# 4a. List the last names of actors, as well as how many actors have that last name.
#___________________________________________________________________________________________________  9 of 29 EX  ____

SELECT last_name as 'Last', Count(last_name) as '# With Same Name'
FROM sakila.actor
GROUP BY last_name;



# 4b. List last names of actors and the number of actors who have that last name, 
#     but only for names that are shared by at least two actors.
#__________________________________________________________________________________________________  10 of 29 EX  ____

SELECT last_name as 'Last', Count(last_name) as '# With Same Name, if Dupl'
FROM sakila.actor
GROUP BY last_name
HAVING Count(last_name) > 1;



# 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. 
#     Write a query to fix the record.
#__________________________________________________________________________________________________  11 of 29 EX  ____

UPDATE sakila.actor
SET first_name = "HARPO"
WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS";



# 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the 
#     correct name after all! In a single query, if the first name of the actor is currently HARPO, 
#     change it to GROUCHO.
#___________________________________________________________________________________________________  12 of 29 EX  ____

UPDATE sakila.actor
SET first_name = "GROUCHO"
WHERE first_name = "HARPO"; # also WHERE actor_id = 172



# 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
#___________________________________________________________________________________________________  13 of 29 EX  ____

DESCRIBE sakila.address;

CREATE TABLE IF NOT EXISTS address (
    address_id SMALLINT(5) UNSIGNED NOT NULL,
    address VARCHAR(50) NOT NULL,
    address2 VARCHAR(50),
    district VARCHAR(20) NOT NULL,
    city_id SMALLINT(5) UNSIGNED NOT NULL,
    postal_code VARCHAR(10),
    phone VARCHAR(20) NOT NULL,
    location GEOMETRY NOT NULL,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (address_id),
    KEY (city_id)
);  # I tried to set location as a second MUL key, but ran into issues ¯\_(ツ)_/¯



# 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. 
#     Use the tables staff and address:
#__________________________________________________________________________________________________  14 of 29 EX  ____

SELECT first_name as "First", last_name as "Last", address as "Address"
FROM address
INNER JOIN staff 
ON address.address_id = staff.address_id;


# 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. 
#     Use tables staff and payment.
#___________________________________________________________________________________________________  15 of 29 EX  ____

SELECT first_name as "First", last_name as "Last", concat('$', format(sum(p.amount), 2)) AS 'Sales Aug 2005'
FROM payment p
INNER JOIN staff s
ON p.staff_id = s.staff_id
WHERE DATE(p.payment_date) > '2005-07-31' AND DATE(p.payment_date) < '2005-09-01'
Group By p.staff_id;
 # CAN and AUS use '$' sign 


# 6c. List each film and the number of actors who are listed for that film. 
#     Use tables film_actor and film. Use inner join.
#_____________________________________________________________________________________________________  16 of 29 EX  ____

SELECT title as 'Title', COUNT(actor_id) as 'Total Actors'
FROM film_actor fa
INNER JOIN film f
ON fa.film_id = f.film_id
GROUP BY f.title;



# 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
#______________________________________________________________________________________________________  17 of 29 EX  ____

SELECT title as 'Title', COUNT(i.film_id) as 'Copies in Stock'
FROM film f
INNER JOIN inventory i
ON f.film_id = i.film_id
GROUP BY f.title
HAVING title = 'Hunchback Impossible';



# 6e. Using the tables payment and customer and the JOIN command, 
#     list the total paid by each customer. 
#     List the customers alphabetically by last name:
#______________________________________________________________________________________________________  18 of 29 EX  ____

SELECT first_name as "First", last_name as "Last", concat('$', format(sum(p.amount), 2)) AS 'Total Purchases'
FROM payment p
INNER JOIN customer c
ON p.customer_id = c.customer_id
Group By p.customer_id
Order by last_name;



# 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
#     As an unintended consequence, films starting with the letters K and Q have 
#     also soared in popularity. Use subqueries to display the titles of movies 
#     starting with the letters K and Q whose language is English.
#_____________________________________________________________________________________________________  19 of 29 EX  ____

SELECT title as 'Title', language_id as 'en Anglais'
FROM film
WHERE title LIKE 'K%' OR title LIKE 'Q%' 
And language_id in
(
 SELECT language_id
  FROM language
  WHERE name IN ('English')
) ; 



# 7b. Use subqueries to display all actors who appear in the film Alone Trip.
#_____________________________________________________________________________________________________  20 of 29 EX  ____

SELECT first_name as "In Alone", last_name as "Trip"
FROM actor
where actor_id in 
(
  SELECT actor_id
  FROM film_actor
  WHERE film_id IN 
  (
  SELECT film_id
  FROM film
  WHERE title IN ('Alone Trip')
  )
); 



# 7c. You want to run an email marketing campaign in Canada, for which you will need 
#     the names and email addresses of all Canadian customers. 
#     Use joins to retrieve this information.
#_____________________________________________________________________________________________________  21 of 29 EX  ____

SELECT first_name as "First", last_name as "Last", email as "Email", country as "Home Country"
from customer cus
JOIN address adr
ON cus.address_id = adr.address_id
JOIN city cty
ON adr.city_id = cty.city_id
JOIN country cnt
on cty.country_id = cnt.country_id
Where cnt.country = 'Canada';



# 7d. Sales have been lagging among young families, and you wish to target all family movies 
#     for a promotion. Identify all movies categorized as family films.
#_____________________________________________________________________________________________________  22 of 29 EX  ____

SELECT title as 'Title'
FROM film 
WHERE film_id IN
(
SELECT film_id FROM film_category
WHERE category_id IN
(
SELECT category_id FROM category
WHERE name = "Family"
));



# 7e. Display the most frequently rented movies in descending order.
#_____________________________________________________________________________________________________  23 of 29 EX  ____

SELECT title as 'Title', COUNT(rental_id) AS 'Rental Count'
FROM rental r
JOIN inventory i
ON r.inventory_id = i.inventory_id
JOIN film f
ON (i.film_id = f.film_id)
GROUP BY f.title
ORDER BY COUNT(rental_id) DESC;



# 7f. Write a query to display how much business, in dollars, each store brought in.
#___________________________________________________________________________________________________  24 of 29 EX  ____

SELECT s.store_id as 'Store ID', concat('$', format(sum(amount), 2)) AS 'Revenue'
FROM payment p
JOIN rental r
ON (p.rental_id = r.rental_id)
JOIN inventory i
ON (i.inventory_id = r.inventory_id)
JOIN store s
ON (s.store_id = i.store_id)
GROUP BY s.store_id; 
 # but have diff exchange rates, so we might need an extra calc converting
 # each sale by date into one or some third currency


# 7g. Write a query to display for each store its store ID, city, and country.
#___________________________________________________________________________________________________  25 of 29 EX  ____

SELECT store_id as 'Store ID', city as 'City', country as 'Country'
FROM store s
JOIN address adr 
ON s.address_id = adr.address_id
JOIN city cty
ON cty.city_id = adr.city_id
JOIN country cnt
ON cnt.country_id = cty.country_id;



# 7h. List the top five genres in gross revenue in descending order. (Hint: you may need 
#     to use the following tables: category, film_category, inventory, payment, and rental.)
#___________________________________________________________________________________________________  26 of 29 EX  ____

SELECT cat.name AS 'Genre', concat('$', format(sum(p.amount), 2)) AS 'Gross' 
FROM category cat
JOIN film_category fcat
ON cat.category_id = fcat.category_id
JOIN inventory i 
ON fcat.film_id=i.film_id
JOIN rental r 
ON i.inventory_id=r.inventory_id
JOIN payment p 
ON r.rental_id=p.rental_id
GROUP BY cat.name 
ORDER BY Gross DESC
LIMIT 5;



# 8a. In your new role as an executive, you would like to have an easy way of viewing 
#     the Top five genres by gross revenue. Use the solution from the problem above to create a view. 
#     If you haven't solved 7h, you can substitute another query to create a view.
#__________________________________________________________________________________________________  27 of 29 EX  ____

CREATE VIEW genre_revenue AS
SELECT cat.name AS 'Genre', concat('$', format(sum(p.amount), 2)) AS 'Gross' 
FROM category cat
JOIN film_category fcat
ON cat.category_id = fcat.category_id
JOIN inventory i 
ON fcat.film_id=i.film_id
JOIN rental r 
ON i.inventory_id=r.inventory_id
JOIN payment p 
ON r.rental_id=p.rental_id
GROUP BY cat.name 
ORDER BY Gross DESC
LIMIT 5;



# 8b. How would you display the view that you created in 8a?
#__________________________________________________________________________________________________  28 of 29 EX  ____

SELECT * FROM genre_revenue;



# 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
#__________________________________________________________________________________________________  29 of 29 EX  ____

DROP VIEW genre_revenue;