import json
import os

FILENAME = "contacts.json"
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []  

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for c in contacts:
        print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    print()


def search_contact(contacts):
    name = input("Enter name to search: ")
    found = False
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"Found: {c['name']} - {c['phone']} - {c['email']}\n")
            found = True
            break
    if not found:
        print("❌ Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            save_contacts(contacts)
            print("🗑️ Contact deleted.\n")
            return
    print("❌ Contact not found.\n")

def main():
    contacts = load_contacts()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
