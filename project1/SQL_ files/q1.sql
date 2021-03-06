/* Set 1 - Question 1
Create a query that lists each movie, the film category it is classified in,
and the number of times it has been rented out.
*/

WITH t1 AS (SELECT title, c.name cat_name, rental_date,rental_id
			FROM film f
			JOIN film_category fc
			ON f.film_id = fc.film_id
			JOIN category c
			ON fc.category_id=c.category_id
			JOIN inventory i
			ON f.film_id=i.film_id
			JOIN rental r
			ON r.inventory_id=i.inventory_id
			WHERE c.name = 'Animation' OR c.name='Children' OR c.name='Classics' OR c.name='Comedy'
		   OR c.name='Family' OR c.name='Music')
SELECT title,cat_name, COUNT(*) rental_count
FROM t1
GROUP BY 1,2
ORDER BY 2 