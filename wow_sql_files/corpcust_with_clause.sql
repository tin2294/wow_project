WITH CorporateCustomers AS (
	SELECT
		first_name,
        last_name,
        email,
        address_houseno,
        address_street,
        address_city,
        address_state,
        address_zipcode,
        company_name,
        emp_id
    FROM auth_user
    JOIN wow_customer
    ON auth_user.id = wow_customer.user_id
	JOIN wow_corpcust
    ON wow_customer.id = wow_corpcust.customer_id
    WHERE wow_customer.cust_type = 'C'
)
SELECT company_name, COUNT(emp_id)
FROM CorporateCustomers
GROUP BY company_name;