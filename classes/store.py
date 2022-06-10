from classes.customer import Customer
from classes.inventory import Inventory

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.customers = Customer.get_all_customers()
        self.inventory = Inventory.get_inventory_list()

    def get_customer_by_id(self, customer_to_find):
        for customer in self.customers:
            if customer.id == customer_to_find:
                return customer

    def add_new_customer(self, customer_data):
        self.customers.append(customer_data)
    
    def return_video_rental(self, video_to_return):
        self.customers.remove(video_to_return)

    def list_inventory(self):
        print("\n")
        for i, video in enumerate(self.inventory):
            print(f"{i + 1}. {video.release_year} {video.title} : {video.copies_available} in stock")