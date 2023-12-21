WITH IndividualCustomers AS (
	SELECT
		first_name,
        last_name,
        email,
        address_houseno,
        address_street,
        address_city,
        address_state,
        address_zipcode,
        license_no,
        insurance_co,
        customer_id
    FROM auth_user
    JOIN wow_customer
    ON auth_user.id = wow_customer.user_id
	JOIN wow_indivcust
    ON wow_customer.id = wow_indivcust.customer_id
)
SELECT insurance_co, COUNT(*) AS "Customer Count"
FROM IndividualCustomers
GROUP BY insurance_co;