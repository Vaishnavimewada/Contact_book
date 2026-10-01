import csv

FILE_NAME = "contactbook.csv"


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()

    phone.isdigit()  # Check if phone number is numeric
    len(phone) == 10  # Check if phone number is 10 digits long

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for existing_contact in reader:
                if existing_contact["name"].lower() == name.lower() or existing_contact["phone"] == phone or existing_contact["email"].lower() == email.lower():
                    print("A contact with this name already exists.")
                    return

    except FileNotFoundError:
        pass  # File doesn't exist yet, so no duplicates


    try:
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "phone", "email"]
            )

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(contact)

        print("Contact added successfully!")

    except OSError as e:
        print(f"Unable to save contact: {e}")


def view_contacts():
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            contacts = list(reader)
            contacts.sort(key=lambda x: x["name"].lower())

            if not contacts:
                print("No contacts found.")
                return

            print("\n----- CONTACTS -----")

            for index, contact in enumerate(contacts, start=1):
                print(
                    f"{index}. "
                    f"Name: {contact['name']}, "
                    f"Phone: {contact['phone']}, "
                    f"Email: {contact['email']}"
                )

    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    search_name = input(
        "Enter the name of the contact to search: "
    ).strip()

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            found_contacts = [
                contact
                for contact in reader
                if contact["name"].lower() == search_name.lower()
            ]

            if not found_contacts:
                print("No contacts found with that name.")
                return

            print("\n----- SEARCH RESULTS -----")

            for index, contact in enumerate(found_contacts, start=1):
                print(
                    f"{index}. "
                    f"Name: {contact['name']}, "
                    f"Phone: {contact['phone']}, "
                    f"Email: {contact['email']}"
                )

    except FileNotFoundError:
        print("No contacts found.")


def delete_contact():
    delete_name = input(
        "Enter the name of the contact to delete: "
    ).strip()

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

        found = False
        remaining_contacts = []

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                found = True
            else:
                remaining_contacts.append(contact)

        if not found:
            print("No contacts found with that name.")
            return

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(remaining_contacts)

        print(f"Contact '{delete_name}' deleted successfully.")

    except FileNotFoundError:
        print("No contacts found.")

def update_contact():
    update_name = input(
        "Enter the name of the contact to update: "
    ).strip()

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

        found = False
        updated_contacts = []

        for contact in contacts:
            if contact["name"].lower() == update_name.lower():
                found = True
                print("Enter new details (leave blank to keep current value):")
                new_name = input(f"New name [{contact['name']}]: ").strip()
                new_phone = input(f"New phone [{contact['phone']}]: ").strip()
                new_email = input(f"New email [{contact['email']}]: ").strip()

                updated_contact = {
                    "name": new_name if new_name else contact["name"],
                    "phone": new_phone if new_phone else contact["phone"],
                    "email": new_email if new_email else contact["email"]
                }
                updated_contacts.append(updated_contact)
            else:
                updated_contacts.append(contact)

        if not found:
            print("No contacts found with that name.")
            return

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(updated_contacts)

        print(f"Contact '{update_name}' updated successfully.")

    except FileNotFoundError:
        print("No contacts found.")

    def show_statistics():
        try:
            with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                contacts = list(reader)

            total_contacts = len(contacts)
            print(f"\nTotal number of contacts: {total_contacts}")

            Gmail_users = [contact for contact in contacts if contact["email"].endswith("@gmail.com")]
            print(f"Number of Gmail users: {len(Gmail_users)}")

            outlook_users = [contact for contact in contacts if contact["email"].endswith("@outlook.com")]
            print(f"Number of Outlook users: {len(outlook_users)}")

            other_email_users = [contact for contact in contacts if not (contact["email"].endswith("@gmail.com") or contact["email"].endswith("@outlook.com"))]
            print(f"Number of users with other email providers: {len(other_email_users)}")

        except FileNotFoundError:
            print("No contacts found.")

def mark_favorite():
    favorite_name = input(
        "Enter the name of the contact to mark as favorite: "
    ).strip()

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

        found = False
        updated_contacts = []

        for contact in contacts:
            if contact["name"].lower() == favorite_name.lower():
                found = True
                contact["favorite"] = "Yes"
            updated_contacts.append(contact)

        if not found:
            print("No contacts found with that name.")
            return

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email", "favorite"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(updated_contacts)

        print(f"Contact '{favorite_name}' marked as favorite.")

    except FileNotFoundError:
        print("No contacts found.")

def view_favorite_contacts():
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

        favorite_contacts = [contact for contact in contacts if contact["favorite"] == "Yes"]

        if not favorite_contacts:
            print("No favorite contacts found.")
        else:
            print("\n===== FAVORITE CONTACTS =====")
            for contact in favorite_contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    except FileNotFoundError:
        print("No contacts found.")
