from contacts import Database, emailIsValid
import sys

db = Database()
if __name__ == "__main__":
        db.create_table()
        try:
            if len(sys.argv) == 2:
                if (sys.argv[1] == "-add"):
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    phone = int(input("Enter phone: "))
                    if emailIsValid(email):
                        db.add_contact(name, phone, email)
                        print("Contact '" + name + "' added")
                    else:
                        print("Error: Invalid email")

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
                    if emailIsValid(email):
                        db.update_contact(sys.argv[2], name, phone, email)
                    else:
                        print("Error: Invalid email")
                elif (sys.argv[1] == "-sn"):
                    db.search_by_name(sys.argv[2])
                else:
                    print("Error: Invalid arguement(s) passed")
            else:
                print("Error: Expected 2 or 3 arguments but got " + str(len(sys.argv)))

        except IndexError:
            print("Error: Expected 1 or 2 arguments but got " + str(len(sys.argv)) + " arguments")
        
        except ValueError:
            print("Error: Phone number must be an integer")

        db.close_connection()