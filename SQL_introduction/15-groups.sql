-- Lists the number of records with the same score in second_table.
-- Displays score and the number of records with the label 'number'.
-- Sorted by the number of records in descending order.
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
