API FOR SECRETARIAT

- register user
- request for, email, phone number, password and confirm password, name (first name, last name, middle name), title, role, band etc
- log a user in

  - log in with email and username and password.

- registration for the following
  - birth notification
    - ask for parent name, house address, contact-phone-number, parent-unit, parent-band, delivery-date, sex(dropdown[male, female]), date-of-naming-ceremony, place-of-naming-ceremony
  - child notification
    - inputs for parent name, child-name, band-of-both-parent([mother, father]), contact-phone-number, date-of-dedication(i can use django auto_now_add= True)
  - marriage thanksgiving
    - inputs for parent name, date of marriage, band-of-both-parents([mother, father]), contact-phone-number([mother, father])
- after each registration, the admin can view the following
  VIEWS
- all registration

- a registration
  - log a user in
  - registration for the following
  - birth notification
  - child notification
  - marriage thanksgiving
- can also delete all registration in all registration
- can also delete just one registration in each registration

URLS

- Have a url for route under registeration registrations
- Have url to get all birth-notification
- Have a url to get one or a specific id of a birth-notification
- Have a url to get all child-notification
- Have a url to get one or a specific child-notification
- Have a url to get all marriage thanksgiving
- Have a url to get one or a specific id for marriage-thanksgiving

VIEWS FOR APIS
STEPS

- import rest framework (follow docs), get routes follow the following

STORING JSON WEB TOKEN
CONNECTING POSTGRES DATABASE

- Download postgres and create a local database on our pc, then do it online with aws(hosting database).
  Use PG-Admin, graphical database

STEPS

- Download Postgres from postgres.org and download pgadmin-4 from pgadmin.org
- Step up the installation process
- Set up a password then remember the password
- Open pgadmin and right click on server, navigate to server and register a new server with information as "name", register localhost and input password and save.
- Naviagate to database and click on create and navigate
- Schemas is wherer the database table will be stored

IN VSCODE

- Navigate to root settings, then make a clone of the database and change engine to "postgresql"
- Then change name to the database name given in pgadmin, in my case "secretariat"
- Add a user, password, host, and port to the database obj(they can be found in the pgadmin created server)
- To make connection, we need a database driver to make the connectionn from django to postgres(database adapter) and its called psycopg2
- Work on it more and more i say
- forgot to push yesterday damn!!!!

