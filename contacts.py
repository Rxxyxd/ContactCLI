import sqlite3
import re
import pandas as pd

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('contacts.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone INTEGER,
            email TEXT,
            unique(phone, email)
            ); ''')
        self.connection.commit()
    
    def add_contact(self, name, phone, email):
        try:
            self.cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
            self.connection.commit()
        
        except sqlite3.IntegrityError:
            print("Error: Contact already exists")
        
        except sqlite3.OperationalError:
            print("Try running - `py main.py -c`")
            print("If this error persists, create an issue on the GitHub repository.")
    
    def get_contacts(self):
        contacts = pd.read_sql_query('SELECT * FROM contacts', self.connection)
        print(contacts)
    
    def delete_contact(self, id):
        try:
            r = self.cursor.execute('SELECT EXISTS(SELECT * FROM contacts WHERE id = ?)', (id,))
            id_exists = list(r.fetchone())
            if id_exists[0] == 1:
                self.cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
                self.connection.commit()
                print("SUCCESS: Contact deleted")
            else:
                print("Error: Contact does not exist")
        except ValueError:
            print("Error: Unable to delete contact")
        except sqlite3.OperationalError:
            print("Try running - `py main.py -c`")
            print("If this error persists, create an issue on the GitHub repository.")

    def update_contact(self, id, name, phone, email):
        try:
            r = self.cursor.execute('SELECT EXISTS(SELECT * FROM contacts WHERE id = ?)', (id,))
            id_exists = list(r.fetchone())
            if id_exists[0] == 1:
                self.cursor.execute('UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?', (name, phone, email, id,))
                self.connection.commit()
            else:
                print("Error: Contact does not exist")
        except sqlite3.OperationalError:
            print("Try running - `py main.py -c`")
            print("If this error persists, create an issue on the GitHub repository.")

    def search_by_name(self, name):
        try:
            r = self.cursor.execute('SELECT * FROM contacts WHERE name = ?', (name,))
            name_exists = list(r.fetchone())
            if name_exists[1] == name:
                contacts = pd.read_sql_query('SELECT * FROM contacts WHERE name =?', self.connection, params=(name,))
                print(contacts)
            else:
                print("Error: Contact does not exist")
        except TypeError:
            print("Error: Contact does not exist")

    def close_connection(self):
        self.connection.close()

def emailIsValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 
    if re.fullmatch(regex, email):
        return True
    else:
        return False