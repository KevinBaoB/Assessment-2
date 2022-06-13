from curses.ascii import isdigit
from classes.customer import Customer
from classes.store import Store


store = Store('CodeBuster')

while True:
    mode = input("\n== Welcome to Code Platoon Video! ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")

    if mode == '1':
        store.list_inventory()

    elif mode == '2':
        customer = input("\nEnter customer information to see their rented videos:\n")
        
        all_id = store.get_all_customer_id()

        while customer not in all_id:
            print("\nACCOUNT NOT IN SYSTEM!\n")
            customer = input("\nEnter customer information to see their rented videos:\n")

        customer_info = (store.get_customer_by_id(customer))
        
        print(customer_info)

        store.customer_current_rentals(customer)

    elif mode == '3':
        customer_data = {}
        
        taken_id = store.get_all_customer_id()

        customer_data['id'] = input('Enter customer ID: \n')

        while customer_data['id'] in taken_id:
            print("ID unavailable! Please select another")
            customer_data['id'] = input('Enter customer ID: \n')

        customer_data['account_type'] = input('Choose from the following customer account types:\n1. "sx" = standard account\n2. "px" = premium account\n3. "sf" = standard family account\n4. "pf" = premium family account\n')

        account_types = ['sx', 'px', 'sf', 'pf']

        while customer_data['account_type'] not in account_types:
            print("Sorry. Please type one of the available account types:\n")

            customer_data['account_type'] = input('Choose from the following customer account types:\n1. "sx" = standard account\n2. "px" = premium account\n3. "sf" = standard family account\n4. "pf" = premium family account\n')

        customer_data['first_name'] = input('Enter customer first name:\n')

        customer_data['last_name'] = input('Enter customer last name: \n')

        # customer_data['current_video_rentals']  = input('Enter any rentals you want now: \n')
    
        store.add_new_customer(Customer(**customer_data))

        print("New account creation Successful!")

    elif mode == '4':
        
        customer_renting = input(f"Enter the ID number of who is renting:\n")

        all_id = store.get_all_customer_id()

        while customer_renting not in all_id:
            print("\nACCOUNT NOT IN SYSTEM!\n")
            customer_renting = input(f"Enter the ID number of who is renting:\n")

        customer = store.get_customer_by_id(customer_renting)

        print(customer)
        store.customer_current_rentals(customer_renting)
        store.available_rentals()

        if store.account_limits_check(customer_renting):
            available_rentals = store.available_video_list()

            video_want_to_rent = input(f"Enter from the available listing above:\n")



            while video_want_to_rent == '' or video_want_to_rent.isspace() or not isdigit(video_want_to_rent) :
                print("\nINVALID INPUT. PLEASE ENTER NUMBER!\n")
                store.available_rentals()
                video_want_to_rent = input(f"\nEnter the NUMBER from the list above:\n")


            while int(video_want_to_rent) > len(available_rentals):
                print("\nINVALID INPUT\n")
                store.available_rentals()
                video_want_to_rent = input(f"Enter from the available listing above:\n")

            else:  
                video_want_to_rent = available_rentals[int(video_want_to_rent) - 1]

            while video_want_to_rent not in available_rentals:
                print("Invalid input. Please choose from the listing!")
                video_want_to_rent = input(f"Enter from the available listing above:\n")
                
            
            while store.rating_check(customer_renting, video_want_to_rent):
                print("RATED R VIDEOS NOT ALLOWED ON YOUR ACCOUNT! ")
                store.available_rentals()
                video_want_to_rent = input(f"Enter from the available listing above thats NOT R-rated:\n")
                while int(video_want_to_rent) > len(available_rentals):
                    print("\nINVALID INPUT\n")
                    store.available_rentals()
                    video_want_to_rent = input(f"Enter from the available listing above:\n")

                else:  
                    video_want_to_rent = available_rentals[int(video_want_to_rent) - 1]

            
            else:
                store.add_video_rental(customer_renting, video_want_to_rent)

        else:
            print("You've reached your max rentals.")

    elif mode == '5':
        who_is_turning_in = input("\nEnter customer ID to see their rented videos:\n")

        all_id = store.get_all_customer_id()

        while who_is_turning_in not in all_id:
            print("\nACCOUNT NOT IN SYSTEM!\n")
            who_is_turning_in = input(f"Enter the ID number of who is turning in:\n")

        customer_info = store.get_customer_by_id(who_is_turning_in)
        rentals = customer_info.current_video_rentals

        print(customer_info)
        store.customer_current_rentals(who_is_turning_in)

# Exact naming for movie returns issue still needs solving

        if len(rentals) > 0:
            video_to_turnin = input("\nPlease enter the number of the video on your current rentals list you would like to turn in: \n")

            while video_to_turnin == '' or video_to_turnin.isspace() or not video_to_turnin.isdigit():
                print("INVALID INPUT. PLEASE ENTER NUMBER!\n")
                store.customer_current_rentals(who_is_turning_in)
                video_to_turnin = input("\nPlease enter the number of the video on your current rentals list you would like to turn in: \n")

            while int(video_to_turnin) > len(rentals):
                print("INVALID INPUT! CHOOSE A NUMBER FROM YOUR LIST!")
                store.customer_current_rentals(who_is_turning_in)
                video_to_turnin = input("\nPlease enter the number of the video on your current rentals list you would like to turn in: \n")

            video_to_turnin = customer_info.current_video_rentals[int(video_to_turnin) - 1]
            
            while video_to_turnin not in customer_info.current_video_rentals:
                print('invalid input. Please name a video:\n')
                video_to_turnin = input("Please enter name of the video you would like to turn in: \n")

            store.return_video_rental(who_is_turning_in, video_to_turnin)
            print("Return Successful!")
        else:
            print("You have nothing to turn in.")
    
    elif mode == '6':
        break