from classes.customer import Customer
from classes.inventory import Inventory

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.customers = Customer.get_all_customers()
        self.inventory = Inventory.get_inventory_list()

    def list_inventory(self):
        print("\n")
        for i, video in enumerate(self.inventory):
            print(f"{i + 1}. {video.release_year} {video.title}")