from contacts import Database, emailIsValid
import argparse

db = Database()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='main.py', description="Contacts Database Arguements")

    # Global Arguements
    parser.add_argument("-c", "--create-table", action="store_true",help="Create Table for Database")
    parser.add_argument("-l", "--list", action="store_true",help="Lists all contacts")

    # Subparser
    subparsers = parser.add_subparsers(title="mode MODE", dest="mode", help="sub-command help. use --set mode MODE to set a default")

    # Create arg parser
    parser_create = subparsers.add_parser("create", help="Create a new contact")
    parser_create.add_argument("--name", required=True, help="Name of contact")
    parser_create.add_argument("--email", required=True, help="Email of contact")
    parser_create.add_argument("--phone", required=True, type=int, help="Phone of contact")

    # delete arg parser
    parser_delete = subparsers.add_parser("delete", help="Delete an existing contact")
    parser_delete.add_argument("--ID", type=int, help="ID of contact")

    # update arg parser
    parser_update = subparsers.add_parser("update", help="Update an existing contact")
    parser_update.add_argument("--id", required=True, type=int, help="ID of contact")
    parser_update.add_argument("--name", required=True, help="Name of contact")
    parser_update.add_argument("--email", required=True, help="Email of contact")
    parser_update.add_argument("--phone", required=True, type=int, help="Phone of contact")

    # read/search arg parser
    parser_read = subparsers.add_parser("search", help="Read an existing contact")
    parser_read.add_argument("--name", help="Search by name of contact")
    #parser_read.add_argument("--ID", type=int, help="Search by ID of contact")
    #parser_read.add_argument("--email", help="Search by email of contact")
    #parser_read.add_argument("--phone", type=int, help="Search by phone of contact")

    args = parser.parse_args()

    # Check what sub-command was used and execute necessary function(s)
    if args.create_table:
        db.create_table()
    elif args.list:
        db.get_contacts()
    
    elif args.mode == "create":
        if emailIsValid(args.email):
            db.add_contact(args.name, args.email, args.phone)
        else:
            print("Invalid email")

    elif args.mode == "delete":
        db.delete_contact(args.id)

    elif args.mode == "update":
        if emailIsValid(args.email):
            db.update_contact(args.id, args.name, args.phone, args.email)
        else:
            print("Invalid email")
    
    elif args.mode == "search":
        print(args.name)
        db.search_by_name(args.name)