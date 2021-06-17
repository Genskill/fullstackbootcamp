# We'll keep all the database specific functions here. In larger
# applications, we might use an object oriented wrapper called an ORM
# to access the database. In that case, all the functions for that
# would be in this module as well.

# Other modules can import this and use the functions here. 
import psycopg2

from flask import current_app, g

# Functions will call get_db to get the database connection. However,
# we don't want a new connection to be created each time this is
# called. Hence, we create the connection and store it in the g
# object. If it's already initialised, we simply return that instead
# of creating a new one.
def get_db():
    if 'db' not in g: # If we've not initialised the database, then
                      # initialise it
        # Notice how we take the name of the database from the
        # config. We initialised this in the __init__.py file.
        dbname = current_app.config['DATABASE'] 
        g.db = psycopg2.connect(f"dbname={dbname}")
    return g.db


