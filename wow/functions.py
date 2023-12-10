from decimal import Decimal


def compute_invoice_amount(overage_rate, start_odom, end_odom, daily_rate, pickup_date, dropoff_date, daily_mil, percentage):
    miles_driven = end_odom - start_odom
    rental_days = (dropoff_date - pickup_date).days
    mile_limit = daily_mil * rental_days
    if miles_driven <= mile_limit:
        total_amount = miles_driven * daily_rate * Decimal(1 - percentage)
    else:
        total_amount = ((miles_driven - mile_limit) * overage_rate + mile_limit * daily_rate) * Decimal(1 - percentage)
    return total_amount
