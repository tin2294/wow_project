WITH VehicleData AS (
	SELECT
		wow_vehicle.make,
        wow_vehicle.model,
        wow_vehicle.year,
        wow_vehicle.lp_state,
        wow_vehicle.lp_number,
        wow_vehicle.vclass_id,
        wow_vclass.class_name,
        wow_vclass.daily_rate,
        wow_vclass.daily_mileage,
        wow_vclass.overage_rate
	FROM wow_vehicle 
	JOIN wow_vclass 
	ON wow_vehicle.vclass_id = wow_vclass.id
)
SELECT
	make,
    model,
    year,
    class_name,
    daily_rate
FROM VehicleData
WHERE daily_rate > ANY (
	SELECT daily_rate
    FROM VehicleData
    WHERE class_name = 'Luxury Sedan'
);