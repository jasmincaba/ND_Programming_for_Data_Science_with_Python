/* Set 1 - Question 2
Provide a table with the movie titles and divide them into 4 levels 
(first_quarter, second_quarter, third_quarter, and final_quarter) 
based on the quartiles (25%, 50%, 75%) of the rental duration for 
movies across all categories
*/

WITH t1 AS(SELECT title, c.name cat_name, rental_duration 
			FROM category c
			JOIN film_category fc
			ON c.category_id=fc.category_id
			JOIN film f
			ON f.film_id=fc.film_id
		    WHERE c.name = 'Animation' OR c.name='Children' OR c.name='Classics' OR c.name='Comedy'
		   OR c.name='Family' OR c.name='Music')
	
SELECT title, cat_name, rental_duration, NTILE(4) OVER(ORDER BY rental_duration) AS standard_quartile
FROM t1
		
