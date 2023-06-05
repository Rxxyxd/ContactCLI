# ContactCLI
A CLI program that stores and retrieves contact information from a database file.

This was created as a learning project for representing database data with pandas and using sqlite3 in python. It is currently a work in progress documentation will be available at a future date. Feel free to report any issues or suggestions to improve my understanding of said libraries in the issues tab. Thank you.

## Available commands

 - `$ py main.py -l` - returns all contacts in the database
 - `$ py main.py delete --id <id>` - deletes a contact from the database by ID
 - `$ py main.py create --name <name> --email <email> --phone <phone> ` - adds a contact to the database
 - `$ py main.py update --id <id> --name <name> --email <email> --phone <phone>` - updates a contact in the database by ID
 - `$ py main.py search --name <name>` - search for contact by name
