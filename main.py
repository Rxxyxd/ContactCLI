from contacts import Database
import sys
import pandas as pd

db = Database()
if __name__ == "__main__":
        db.create_table()
        try:
            if len(sys.argv) == 2:
                if (sys.argv[1] == "-add"):
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    db.add_contact(name, phone, email)
                    print("Contact '" + name + "' added")

                elif (sys.argv[1] == "-l"):
                    contacts = pd.read_sql_query("SELECT * FROM contacts", db.connection)
                    print(contacts)

            elif(len(sys.argv) == 3):
                if (sys.argv[1] == "-d"):
                    db.delete_contact(sys.argv[2])
                elif (sys.argv[1] == "-u"):
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    db.update_contact(sys.argv[2], name, phone, email)
            else:
                print("Error: Expected 1 or 2 arguments but got " + str(len(sys)))

        except IndexError:
            print("Error: Expected 1 or 2 arguments but got " + str(len(sys.argv)) + " arguments")
        db.close_connection()