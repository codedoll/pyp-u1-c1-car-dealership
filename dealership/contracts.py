# A customer can either buy or lease a car. There are two types of contracts to support such operations: BuyContract and LeaseContract. A contract will have two important methods:

# total_value() is the total value of the contract to pay by a customer.
# monthly_value() is the amount of money that a customer is supposed to pay monthly.
# Each contract will have a different way to compute its value. But for both of them the value will depend of the price of the vehicle (discussed above) and the type of Customer. If the customer is an Employee, the contract will have a final discount of 10%. If the customer is a regular Customer, there's no discount applied.
class Contract(object):
    pass



# Buy Contracts

# A BuyContract is created by passing the following attributes:

# customer: Either a regular Customer or an Employee
# vehicle: The vehicle involved in the transaction.
# monthly_payments: How many months the customer is going to take to pay for the whole contract. Example, if monthly_payments is 2, the customer will take two months to pay for it.
# The total_value() of a BuyContract will be computed in this way: vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee). In this case I is the interest rate applied and it will vary depending of the type of vehicle:

# Car: 7% monthly (1.07)
# Motorcycle: 3% monthly (1.03)
# Truck: 11% monthly (1.11)
# The monthly_value of the contract will be just the total value divided by the amount of months: total_value() / monthly_payments.

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        pass


# Lease Contracts

# A LeaseContract is created by passing the following attributes:

# customer: Either a regular Customer or an Employee
# vehicle: The vehicle involved in the transaction.
# length_in_months: How many months the customer is going to lease the vehicle.
# The total_value() of a LeaseContract will be computed in this way: vehicle.sale_price() + (lease_multiplier) - (discount if employee) *. In this case lease_multiplier depends on the vehicle and is computed in the following way:

# Car: sale_price() + (sale_price() * 1.2 / length_in_months).
# Motorcycle: sale_price() + (sale_price() * 1 / length_in_months)
# Truck: sale_price() + (sale_price() * 1.7 / length_in_months)
# The monthly_value of the contract will be just the total value divided by the amount of months: total_value() / length_in_months.

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass
