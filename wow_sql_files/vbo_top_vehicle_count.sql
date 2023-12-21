SELECT 
	office_id, 
    address_houseno, 
    address_street, 
    address_city, 
    address_state, 
    address_zipcode, 
    COUNT(vehicle_id) AS "Vehicle Count"
FROM vehicle_by_office_and_vclass
GROUP BY office_id, address_houseno, address_street, address_city, address_state, address_zipcode
HAVING COUNT(vehicle_id) > (
	SELECT AVG(vehicle_count) FROM (
		SELECT COUNT(vehicle_id) AS vehicle_count
        FROM vehicle_by_office_and_vclass
        GROUP BY office_id
    ) AS subquery
)
ORDER BY COUNT(vehicle_id) DESC;