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

    def get_all_customer_id(self):
        print("\n")
        id_list = []
        for i, customer in enumerate(self.customers):
            id_list.append(customer.id)
        return id_list

    def get_movie_by_title(self, title):
        for video in self.inventory:
            if video.title == title:
                return video

    def add_new_customer(self, customer_data):
        self.customers.append(customer_data)
    
    def add_video_rental(self,customer, video_to_rent):
        self.get_customer_by_id(customer).current_video_rentals.append(video_to_rent)        
        self.get_movie_by_title(video_to_rent).copies_available = (int(self.get_movie_by_title(video_to_rent).copies_available) - 1)
        return self.get_customer_by_id(customer).current_video_rentals


    def return_video_rental(self,customer, video_to_return):
        self.get_customer_by_id(customer).current_video_rentals.remove(video_to_return)
        self.get_movie_by_title(video_to_return).copies_available = (int(self.get_movie_by_title(video_to_return).copies_available) + 1)


    def available_rentals(self):
        count = 0
        print("\n")
        print("The available rentals are:\n")
        for i, video in enumerate(self.inventory):
            if video.copies_available != "0":
                count += 1
                print(f"{count}. {video.title} with {video.copies_available} in stock")


    def list_inventory(self):
        print("\n")
        for i, video in enumerate(self.inventory):
            print(f"{i + 1}. {video.release_year} {video.title} : {video.copies_available} in stock")
