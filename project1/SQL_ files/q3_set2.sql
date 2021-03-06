/* Set 2 - Question 3
For each of these top 10 paying customers,  find out the difference 
across their monthly payments during 2007. Write a query to compare the 
payment amounts in each successive month.
*/

WITH t1 AS (SELECT c.customer_id,concat(c.first_name,' ',c.last_name)full_name,sum(amount)pay_amount
			FROM payment p
			JOIN customer c
			ON p.customer_id=c.customer_id
			GROUP BY 1,2
			ORDER BY 3 DESC
			LIMIT 10),
	t2 AS(SELECT DISTINCT DATE_TRUNC('month',payment_date) AS pay_mon, full_name,
					COUNT(payment_date)OVER(PARTITION BY DATE_TRUNC('month',payment_date),full_name) AS pay_countpermont, 
					SUM(amount) OVER(PARTITION BY DATE_TRUNC('month',payment_date),full_name) AS pay_am
			FROM t1
			JOIN payment p
			ON t1.customer_id=p.customer_id
			ORDER BY 2)	
SELECT pay_mon,full_name,  pay_am, LAG(pay_am) OVER(PARTITION BY full_name) AS lag,
		(pay_am-LAG(pay_am) OVER(PARTITION BY full_name)) AS diff_by_month
FROM t2
ORDER BY diff_by_month DESC
		