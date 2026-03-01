def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact saved!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            print("\n--- Contact List ---")
            for line in file:
                name, phone, email = line.strip().split(",")
                print(f"Name: {name}")
                print(f"Phone: {phone}")
                print(f"Email: {email}")
                print("-" * 20)
    except FileNotFoundError:
        print("No contacts found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")