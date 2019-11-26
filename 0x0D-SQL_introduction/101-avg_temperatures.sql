-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Results should display the city and avg_temp (in this order)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
