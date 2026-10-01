import contacts


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Statistics")
    print("7. Mark Contact as Favorite")
    print("8. View Favorite Contacts")  
    print("9. Exit")


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                contacts.add_contact()

            elif choice == 2:
                contacts.view_contacts()

            elif choice == 3:
                contacts.search_contact()

            elif choice == 4:
                contacts.delete_contact()

            elif choice == 5:
                contacts.update_contact()

            elif choice == 6:
                contacts.show_statistics()

            elif choice == 7:
                contacts.mark_favorite()

            elif choice == 8:
                contacts.view_favorite_contacts()

            elif choice == 9:
                print("Exiting the Contact Book. Goodbye!")
                break

            else:
                print("Invalid choice! Please choose between 1 and 9.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()