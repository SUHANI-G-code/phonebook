phonebook = {}
def create_contact():
  n= int(input("How many contacts do you want to add? "))
  for i in range(n):
      name = input(f"Enter name for contact {i+1}: ")
      contact_number = int(input(f"Enter phone number for {name}: "))
      if name in phonebook:
         print(f"contact {name} already exits!")
      else:
          phonebook[name]=contact_number
          print(f"contact {name} added successfully!")
def delete_contact(name):
     if name in phonebook:
        del phonebook[name]
        print(f"contact {name} is deleted succesfully.")
     else:
       print(f"contact {name} does not exist.")

def search_contacts():
    name=input("enter the contact name you want to view:")
    if name in phonebook:
        print(f"Contact {name} : {phonebook[name]}")
    else:
       print(f"contact {name} does not exist.")
  
def update_contact(name,new_contact_number):
        if name in phonebook:
           phonebook[name]= new_contact_number
           print(f"contact {name} updated successfully.")
        else:
           print(f"contact {name} does not exist.")
def display_all_contacts():
   if not phonebook:
      print("no contact found")
   else:
      print("all contacts:")
      for name,contact_number in phonebook.items():
          print(f"{name} : {contact_number}")

def main():
       while True:
           print("\nPhonebook Menu:")
           print("1. Create Contact")
           print("2. Delete Contact")
           print("3. Search Contact")
           print("4. Update Contact")
           print("5. Display All Contacts")
           print("6. Exit")
           
           choice = input("Enter your choice (1-6): ").strip() 
           
           if choice =='1':
               create_contact()
           elif choice =='2':
               name = input("Enter contact name to delete: ")
               delete_contact(name)
           elif choice =='3':
               search_contacts()
           elif choice =='4':
               name = input("Enter contact name to update: ")
               new_contact_number = input("Enter new contact number: ")
               update_contact(name, new_contact_number)
           elif choice =='5':
               display_all_contacts()
           elif choice =='6':
               print("Exiting phonebook.")
               break
           else:
               print("Invalid choice, please try again.")

main()