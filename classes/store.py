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

    def account_limits_check(self, customer):
        customer_info = self.get_customer_by_id(customer)
        rentals = customer_info.current_video_rentals
        account_type = customer_info.account_type
        if account_type == 'sx' and len(rentals) < 1:
            return True
        elif account_type == 'px' and len(rentals) < 3:
            return True
        elif account_type == 'sf' and len(rentals) < 1:
            return True
        elif account_type == 'pf' and len(rentals) < 3:
            return True
        else:
            return False

    def rating_check(self, customer, video_to_rent):
        customer_info = self.get_customer_by_id(customer)
        account_type = customer_info.account_type
        movie = self.get_movie_by_title(video_to_rent)
        
        if account_type == 'sf' and movie.rating == 'R':
            return True
        elif account_type == 'pf' and movie.rating == 'R':
            return True

    def add_video_rental(self,customer, video_to_rent):
        movie = self.get_movie_by_title(video_to_rent)
        current_rentals = self.get_customer_by_id(customer).current_video_rentals
        if movie.copies_available != "0":
            movie.copies_available = (int(self.get_movie_by_title(video_to_rent).copies_available) - 1)
            current_rentals.append(video_to_rent) 

        else :
            print("\nNone in stock\n")
        
        if len(current_rentals) == 0:
            print("You have no rentals")
        else:
            print("Rental Succussful!\n")


    def return_video_rental(self,customer, video_to_return):
        self.get_customer_by_id(customer).current_video_rentals.remove(video_to_return)
        self.get_movie_by_title(video_to_return).copies_available = (int(self.get_movie_by_title(video_to_return).copies_available) + 1)

    def customer_current_rentals(self,customer):
        customer_info = self.get_customer_by_id(customer)
        if customer_info.current_video_rentals == ['']:
            customer_info.current_video_rentals = []
            print("Zero rentals in this account.")

        elif len(customer_info.current_video_rentals) != 0:
            for i, video in enumerate(customer_info.current_video_rentals):
                print(f"{i + 1}. {video}")
        
        else:
            print("Zero rentals in this account.")

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
