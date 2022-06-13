import csv
import os

class Customer:
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals = []):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        if self.current_video_rentals == [''] or self.current_video_rentals == "":
            self.current_video_rentals = []
        else:
            self.current_video_rentals = ("".join(self.current_video_rentals)).split("/")


# When called for the customer class info for an individual customer
    
    def __str__(self):
        return f"\n{self.first_name} {self.last_name} is renting:\n"
        
# Used to get all customers info in the store class
 
    @classmethod
    def get_all_customers(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as customer_file:
            cust_reader = csv.DictReader(customer_file)
            for customer in cust_reader:
                customers.append(Customer(**dict(customer)))
        return customers
