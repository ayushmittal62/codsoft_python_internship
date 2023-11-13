#contact book
import tkinter as tk

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    
    name_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    
    update_contact_list()

def update_contact_list():
    contact_list.delete(0, 'end')
    for contact in contacts:
        contact_list.insert('end', f"{contact.name}: {contact.phone}")

def search_contact():
    search_term = search_entry.get()
    search_results = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    update_search_results(search_results)

def update_search_results(results):
    search_list.delete(0, 'end')
    for result in results:
        search_list.insert('end', f"{result.name}: {result.phone}")

def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        updated_name = updated_name_entry.get()
        updated_phone = updated_phone_entry.get()
        contact = contacts[selected_index]
        contact.name = updated_name
        contact.phone = updated_phone
        update_contact_list()

def delete_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        contacts.pop(selected_index)
        update_contact_list()

app = tk.Tk()
app.title("Contact Book")

name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1)

address_label = tk.Label(app, text="Address:")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(app)
address_entry.grid(row=3, column=1)

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2)

contact_list = tk.Listbox(app)
contact_list.grid(row=0, column=2, rowspan=5, columnspan=2)
update_contact_list()

search_label = tk.Label(app, text="Search:")
search_label.grid(row=5, column=0)
search_entry = tk.Entry(app)
search_entry.grid(row=5, column=1)

search_button = tk.Button(app, text="Search", command=search_contact)
search_button.grid(row=5, column=2)

search_list = tk.Listbox(app)
search_list.grid(row=6, column=0, rowspan=5, columnspan=4)

update_label = tk.Label(app, text="Update Name:")
update_label.grid(row=11, column=0)
updated_name_entry = tk.Entry(app)
updated_name_entry.grid(row=11, column=1)

update_phone_label = tk.Label(app, text="Update Phone:")
update_phone_label.grid(row=12, column=0)
updated_phone_entry = tk.Entry(app)
updated_phone_entry.grid(row=12, column=1)

update_button = tk.Button(app, text="Update Contact", command=update_selected_contact)
update_button.grid(row=13, column=0, columnspan=2)

delete_button = tk.Button(app, text="Delete Contact", command=delete_selected_contact)
delete_button.grid(row=14, column=0, columnspan=2)

app.mainloop()
