CREATE OR REPLACE VIEW vehicle_by_office_and_vclass AS
	SELECT
		wow_office.id as "office_id",
		wow_office.address_houseno,
        wow_office.address_street,
        wow_office.address_city,
        wow_office.address_state,
        wow_office.address_zipcode,
        wow_vehicle.id as "vehicle_id",
        wow_vehicle.make,
        wow_vehicle.model,
        wow_vehicle.year,
        wow_vclass.id as "vclass_id",
        wow_vclass.class_name,
        wow_vclass.daily_rate,
        wow_vclass.daily_mileage
	FROM wow_office
	JOIN wow_vehicle
	ON wow_office.id = wow_vehicle.office_id
    JOIN wow_vclass
    ON wow_vclass.id = wow_vehicle.vclass_id;