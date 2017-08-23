class Person(object):
    def __init__(self, first_name, last_name, email, is_employee=Null):        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_employee = is_employee

class Customer(Person):
    def __init__(self, first_name, last_name, email):
        super(Customer, self).__init__(first_name, last_name, email, is_employee)
        self.is_employee = False

class Employee(Person):
    def __init__(self, first_name, last_name, email):
	    super(Employee, self).__init__(first_name, last_name, email)
        self.is_employee = True