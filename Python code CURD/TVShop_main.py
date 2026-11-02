# main.py
# This is the main program. It shows a menu to the user
# and calls the CRUD functions written in TVShop_module.py.

import TVShop_module as tm


def show_menu():
    print("\n===== TV Shop Inventory System =====")
    print("1. Add TV")
    print("2. View All TVs")
    print("3. Update TV")
    print("4. Delete TV")
    print("5. Search TV")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            brand = input("Enter TV brand: ")
            model = input("Enter TV model: ")
            screen_size = input("Enter screen size: ")
            price = input("Enter TV price: ")
            tm.add_tv(brand, model, screen_size, price)

        elif choice == "2":
            tm.view_tvs()

        elif choice == "3":
            try:
                tv_id = int(input("Enter TV ID to update: "))
            except ValueError:
                print("\nPlease enter a valid number for TV ID.")
                continue

            print("Leave a field blank if you don't want to change it.")
            brand = input("New brand: ") or None
            model = input("New model: ") or None
            screen_size = input("New screen size: ") or None
            price = input("New price: ") or None
            status = input("New status (Available/Sold): ") or None

            tm.update_tv(tv_id, brand, model, screen_size, price, status)

        elif choice == "4":
            try:
                tv_id = int(input("Enter TV ID to delete: "))
            except ValueError:
                print("\nPlease enter a valid number for TV ID.")
                continue

            tm.delete_tv(tv_id)

        elif choice == "5":
            try:
                tv_id = int(input("Enter TV ID to search: "))
            except ValueError:
                print("\nPlease enter a valid number for TV ID.")
                continue

            tv = tm.search_tv(tv_id)

            if tv:
                print(f"\nFound: {tv}")
            else:
                print(f"\nNo TV found with ID {tv_id}.")

        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1-6.")


if __name__ == "__main__":
    main()
