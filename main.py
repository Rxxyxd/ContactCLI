from contacts import Database
import sys

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
                    db.get_contacts()
                
                else:
                    print("Error: Invalid arguement(s) passed")

            elif(len(sys.argv) == 3):
                if (sys.argv[1] == "-d"):
                    db.delete_contact(sys.argv[2])
                elif (sys.argv[1] == "-u"):
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    db.update_contact(sys.argv[2], name, phone, email)
                elif (sys.argv[1] == "-sn"):
                    db.search_by_name(sys.argv[2])
                else:
                    print("Error: Invalid arguement(s) passed")
            else:
                print("Error: Expected 2 or 3 arguments but got " + str(len(sys.argv)))

        except IndexError:
            print("Error: Expected 1 or 2 arguments but got " + str(len(sys.argv)) + " arguments")

        db.close_connection()