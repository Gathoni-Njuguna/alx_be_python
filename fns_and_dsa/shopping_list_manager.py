def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            if item:
                shopping_list.append(item)
            pass
        elif choice == '2':
           
            if not shopping_list:
                print("empty")
            else:
                print("Here is your list:")
                print(shopping_list)  # Show the list first
                # remov = input("Enter item to remove: ")  # Then ask for input
            # if remov in shopping_list:
            #     shopping_list.remove(remov)
            # else:
            #     print("Item not found")
            pass
        elif choice == '3':
            if not shopping_list:
                print("empty")
            else:
                print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()