SELECT 
	id, 
    class_name, 
    daily_rate, 
    daily_mileage, 
    daily_rate * 5 + overage_rate * 0 AS "Total for 5 days and 50 miles over",
    overage_rate
FROM wow_vclass
WHERE daily_rate * 5 + overage_rate * 0 = (
	SELECT MIN(daily_rate * 5 + overage_rate * 0)
    FROM wow_vclass
);