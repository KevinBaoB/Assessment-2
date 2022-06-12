import csv
import os

# Manage customer information:
# customer id
# customer account type (sx/px/sf/pf)
# "sx" = standard account: max 1 rental out at a time
# "px" = premium account: max 3 rentals out at a time
# "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
# "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies
# customer first name
# customer last name
# current list of video rentals (by title), each title separated by a forward slash "/"
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
    
    def __str__(self):
        return f"\n{self.first_name} {self.last_name} is renting {', '.join(self.current_video_rentals) if len(', '.join(self.current_video_rentals)) != 0 else 'nothing at this time'}"
    
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
