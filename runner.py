from classes.customer import Customer
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

    elif mode == '2':
        customer = input("\nEnter customer information to see their rented videos:\n")
        customer_info = store.get_customer_by_id(customer)
        print(f"\n{customer_info.first_name} {customer_info.last_name} is renting {customer_info.current_video_rentals}\n")

    elif mode == '3':
        customer_data = {'role': 'customer'}
        customer_data['id'] = input('Enter customer id: \n')
        customer_data['account_type'] = input('Choose from the following customer account types:\n1. "sx" = standard account\n2. "px" = premium account\n3. "sf" = standard family account\n4. "pf" = premium family account\n')
        customer_data['first_name']      = input('Enter customer first name:\n')
        customer_data['last_name']       = input('Enter customer last name: \n')
        customer_data['current_video_rentals']  = input('Enter any rentals you want now: \n')
    
        store.add_new_customer(Customer(**customer_data))


    elif mode == '5':
        who_is_turning_in = input("\nEnter customer information to see their rented videos:\n")
        customer_info = store.get_customer_by_id(who_is_turning_in)
        print(f"\n{customer_info.first_name} {customer_info.last_name} is renting {customer_info.current_video_rentals}\n")

        video_to_turnin = input("Please enter name of the video you would like to turn in: \n")
        store.return_video_rental(video_to_turnin)   
    
    elif mode == '6':
        break