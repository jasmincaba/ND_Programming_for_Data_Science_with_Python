/* Set 2 - Question 1 
Write a query that returns the store ID for the store, 
the year and month and the number of rental orders each
store has fulfilled for that month.
*/
WITH t1 AS (SELECT s.store_id , rental_date
		FROM store s
		JOIN staff
		ON s.store_id=staff.store_id
		JOIN rental r
		ON staff.staff_id=r.staff_id),
	 t2 AS (SELECT store_id,DATE_PART('year',rental_date) AS rental_year,
			DATE_PART('month',rental_date) AS rental_month
		FROM t1)
		
SELECT DISTINCT rental_month, rental_year, store_id, COUNT(*) OVER(PARTITION BY rental_year,rental_month,store_id) AS count_rentals
FROM t2
ORDER BY count_rentals DESC