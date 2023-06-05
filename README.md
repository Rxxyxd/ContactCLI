# ContactCLI
A CLI program that stores and retrieves contact information from a database file.

This was created as a learning project for representing database data with pandas and using sqlite3 in python. It is currently a work in progress documentation will be available at a future date. Feel free to report any issues or suggestions to improve my understanding of said libraries in the issues tab. Thank you.

## Set-Up

Upon first use make sure you create the database table for your contacts by running:
`py main.py -c`
Without doing this could cause some sqlite errors.

## Available commands

 - `$ py main.py -h --help` - returns help message
 - `$ py main.py -l --list` - returns all contacts in the database
 - `$ py main.py -c --create-table` - creates database table
 - `$ py main.py delete --id <id>` - deletes a contact from the database by ID
 - `$ py main.py create --name <name> --email <email> --phone <phone> ` - adds a contact to the database
 - `$ py main.py update --id <id> --name <name> --email <email> --phone <phone>` - updates a contact in the database by ID
 - `$ py main.py search --name <name>` - search for contact by name
