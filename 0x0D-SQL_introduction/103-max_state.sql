-- Write a script that displays the max temperature of each state (ordered by State name).
-- Results should display the state and the max_temp (in this order)
SELECT state, MAX(value)  max_temp FROM temperatures GROUP BY state ORDER BY state;
