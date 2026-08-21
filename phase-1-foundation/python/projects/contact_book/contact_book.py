import json

def menu():
    while True:
        userInput = int(input("Enter A Number:\n1. Add Contact\n2. View All Contacts\n3. Search Contact\n4. Delete Contact"))
        if userInput == 1:
            add_contact()
        elif userInput == 2:
            view_contact()
        elif userInput == 3:
            search_contact()
        elif userInput == 4:
            delete_contact()

     



def view_contact():
    with open("contact.json","r") as file:
        content = json.load(file)

    iter = 1
    for person in content:
        print(iter, ".", person["name"], person["number"], "\n")
        iter += 1


def search_contact():
    with open("contact.json","r") as file:
            content = json.load(file)
    
    contact_name = input("Enter the name of the contact: ")
    for person in content:
        if(person["name"] == contact_name):
            print("\n", person["name"], person["number"], "\n")


def delete_contact():
    with open("contact.json","r") as file:
            content = json.load(file)
    
    contact_name = input("Enter the name of the contact to delete: ")
    iter = 0
    for person in content:
        if(person["name"] == contact_name):
            removed = content.pop(iter)
            print(removed)
            with open("contact.json", "w") as file:
                json.dump(content, file)
        iter += 1


def add_contact():
    with open("contact.json","r") as file:
            content = json.load(file)
    
    contact_name = input("Enter the name of the contact: ")
    contact_number = input("Enter the number of the contact: ")
    new_entry = {"name":contact_name, "number":contact_number}
    content.insert(len(content), new_entry)

    with open("contact.json", "w") as file:
        json.dump(content, file)  
    


menu()

