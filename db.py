import sqlite3

class Database():
    def __init__(self):
        try:
            self.connection = sqlite3.connect('contacts.db')
            self.cursor = self.connection.cursor()
        
        except:
            print("Error: Unable to connect to database")

    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                email TEXT,
                unique(phone, email)
                ); ''')
            self.connection.commit()
        except:
            print("Error: Unable to create table")
    
    def add_contact(self, name, phone, email):
        try:
            self.cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Error: Contact already exists")
    
    def get_contacts(self):
        try:
            self.cursor.execute('SELECT * FROM contacts')
            contacts = self.cursor.fetchall()
            return contacts
        except:
            print("No contacts found")
    
    def delete_contact(self, id):
        try:
            self.cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
            self.connection.commit()
        except:
            print("Error: Unable to delete contact")

    def update_contact(self, id, name, phone, email):
        try:
            self.cursor.execute('UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?', (name, phone, email, id))
            self.connection.commit()
        except:
            print("Error: Unable to update contact")

    def close_connection(self):
        self.connection.close()