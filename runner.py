from classes.customer import Customer
from classes.store import Store
# Viewing the current video inventory for the store X
# Viewing a customer's current rented videos X
# customer by id X
# each title should be listed separately (i.e. not displayed with slashes from the CSV file) X
# Adding a new customer X
# you should not have an initial list of video rentals assigned to a newly created customer X
# can you prevent duplicate ids from existing? X
# Renting a video out to a customer X
# video by title X
# customer by id X
# IMPORTANT: Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video! X
# Returning a video from a customer X
# video by title X
# customer by id X
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

        customer_info = str(store.get_customer_by_id(customer))

        print(customer_info)

    elif mode == '3':
        customer_data = {}
        
        taken_id = store.get_all_customer_id()

        customer_data['id'] = input('Enter customer ID: \n')

        while customer_data['id'] in taken_id:
            print("ID unavailable! Please select another")
            customer_data['id'] = input('Enter customer ID: \n')

        customer_data['account_type'] = input('Choose from the following customer account types:\n1. "sx" = standard account\n2. "px" = premium account\n3. "sf" = standard family account\n4. "pf" = premium family account\n')

        account_types = ['sx', 'fx', 'sf', 'pf']

        while customer_data['account_type'] not in account_types:
            print("Sorry. Please type one of the available account types:\n")

            customer_data['account_type'] = input('Choose from the following customer account types:\n1. "sx" = standard account\n2. "px" = premium account\n3. "sf" = standard family account\n4. "pf" = premium family account\n')

        customer_data['first_name'] = input('Enter customer first name:\n')

        customer_data['last_name'] = input('Enter customer last name: \n')

        # customer_data['current_video_rentals']  = input('Enter any rentals you want now: \n')
    
        store.add_new_customer(Customer(**customer_data))

    elif mode == '4':
        store.available_rentals()

        customer_renting = input(f"Enter the ID number of who is renting:\n")

        customer = store.get_customer_by_id(customer_renting)

        print(customer)

        if store.account_limits_check(customer_renting):
            video_want_to_rent = input(f"Enter from the available listing above:\n")
            
            if store.rating_check(customer_renting, video_want_to_rent):
                print("Rated R videos are not apart of your account")
            
            else:
                store.add_video_rental(customer_renting, video_want_to_rent)

        else:
            print("You've reached your max rentals.")

    elif mode == '5':
        who_is_turning_in = input("\nEnter customer information to see their rented videos:\n")

        customer_info = store.get_customer_by_id(who_is_turning_in)
        rentals = ", ".join(customer_info.current_video_rentals)

        print(f"\n{customer_info.first_name} {customer_info.last_name} is renting {rentals}\n")

# Exact naming for movie returns issue still needs solving

        if len(rentals) > 0:
            video_to_turnin = input("Please enter name of the video you would like to turn in: \n")
            
            while video_to_turnin not in customer_info.current_video_rentals:
                print('invalid input. Please name a video:\n')
                video_to_turnin = input("Please enter name of the video you would like to turn in: \n")

            store.return_video_rental(who_is_turning_in,video_to_turnin)
        else:
            print("You have nothing to turn in.")
    
    elif mode == '6':
        break