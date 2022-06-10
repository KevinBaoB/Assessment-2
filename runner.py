from classes.customer import Customer
from classes.inventory import Inventory
from classes.store import Store
# Viewing the current video inventory for the store
# Viewing a customer's current rented videos
# customer by id
# each title should be listed separately (i.e. not displayed with slashes from the CSV file)
# Adding a new customer
# you should not have an initial list of video rentals assigned to a newly created customer
# can you prevent duplicate ids from existing?
# Renting a video out to a customer
# video by title
# customer by id
# IMPORTANT: Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!
# Returning a video from a customer
# video by title
# customer by id
# Exiting the application


# == Welcome to Code Platoon Video! ==
# 1. View store video inventory
# 2. View customer rented videos
# 3. Add new customer
# 4. Rent video
# 5. Return video
# 6. Exit

store = Store('CodeBuster')

while True:
    mode = input("\n== Welcome to Code Platoon Video! ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")

    if mode == '1':
        store.list_inventory()
    
    elif mode == '6':
        break