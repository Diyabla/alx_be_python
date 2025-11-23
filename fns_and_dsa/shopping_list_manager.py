def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")
            print()

        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print("Item not found in the list.")
            print()

        elif choice == "3":
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("Shopping list:")
                for item in shopping_list:
                    print(f"- {item}")
            print()

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")
            print()


if __name__ == "__main__":
    main()
