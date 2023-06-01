import db
import sys

database = db.Database()

if __name__ == "__main__":
        database.create_table()
        try:
            if (sys.argv[1] == "-d"):
                database.delete_contact(sys.argv[2])
            elif (sys.argv[1] == "add"):
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                database.add_contact(name, phone, email)
            elif (sys.argv[1] == "-a"):
                print(database.get_contacts())
            else:
                print("Error: Invalid arguement(s)")
        except IndexError:
            print("Error: Expected 1 or 2 arguments but got " + str(len(sys.argv)) + " arguments")