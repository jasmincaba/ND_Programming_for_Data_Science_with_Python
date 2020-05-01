/* Set 2 - Question 2
Write a query to capture the customer name, month and year of payment, 
and total payment amount for each month by these top 10 paying customers
*/

WITH t1 AS (SELECT c.customer_id,concat(c.first_name,' ',c.last_name)full_name,sum(amount)pay_amount
			FROM payment p
			JOIN customer c
			ON p.customer_id=c.customer_id
			GROUP BY 1,2
			ORDER BY 3 DESC
			LIMIT 10)
			
SELECT DISTINCT DATE_TRUNC('month',payment_date) AS pay_mon, full_name,
					COUNT(payment_date)OVER(PARTITION BY DATE_TRUNC('month',payment_date),full_name) AS pay_countpermont, 
					SUM(amount) OVER(PARTITION BY DATE_TRUNC('month',payment_date),full_name) AS pay_am
FROM t1
JOIN payment p
ON t1.customer_id=p.customer_id
ORDER BY 2

