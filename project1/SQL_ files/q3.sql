/* Set 1 - Question 3
Provide a table with the family-friendly film category, each of the quartiles,
and the corresponding count of movies within each combination of film category 
for each corresponding rental duration category
*/

WITH t1 AS(SELECT title, c.name cat_name, rental_duration 
			FROM category c
			JOIN film_category fc
			ON c.category_id=fc.category_id
			JOIN film f
			ON f.film_id=fc.film_id
		    WHERE c.name = 'Animation' OR c.name='Children' OR c.name='Classics' OR c.name='Comedy'
		   OR c.name='Family' OR c.name='Music'),
	 t2 AS(SELECT title, cat_name, rental_duration, NTILE(4) OVER(ORDER BY rental_duration) AS standard_quartile
			FROM t1)

SELECT DISTINCT cat_name, standard_quartile, COUNT(*) OVER(PARTITION BY cat_name,standard_quartile)AS count
FROM t2
ORDER BY 1,2