# We'll keep all the database specific functions here. In larger
# applications, we might use an object oriented wrapper called an ORM
# to access the database. In that case, all the functions for that
# would be in this module as well.

# Other modules can import this and use the functions here. 
import psycopg2

# click is a library installed as a dependency of flask which is used
# to add extra commands to the flask executable. We already have
# "flask run" but we can add more commands like "flask initdb" etc.
import click 
from flask import current_app, g
from flask.cli import with_appcontext

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


# This function will close the database connection and remove the "db"
# object from g so that if get_db is called again, it will get
# reinitialised.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# This function will initialise the database. It will drop any tables
# that are there and then run the provided SQL file to create the
# database
def init_db():
    db = get_db()
    # The current_app object gives us the instance of the app through
    # which this is being run. This is different from just importing
    # and running. We use "flask run" so these functions are being
    # executed by flask. current_app gives us that flask app through
    # which these functions are being called.
    #
    # In my case, the 000_create_sql file is in
    # /home/noufal/projects/lycaeum/genskill/2021-live/bootcamp/classes/15-June/jobs/sql. It
    # will be different for you and if I write this in my program, it
    # won't work. I cannot simply type "sql/000_create.sql" either
    # since our program will be started from some other directory. I
    # need to know where *this* file (db.py) is and then find the sql/
    # directory inside the directory where db.py is. Then find the
    # file 000_create.sql inside that directory. current_app is
    # something that flask provides to take care of this for me.
    f = current_app.open_resource("sql/000_create.sql")
    sql_code = f.read().decode("ascii")
    cur = db.cursor()
    cur.execute(sql_code)
    cur.close()
    db.commit()
    close_db()

# All flask commands cannot be run separately. If we simply import this file and try to run things, it will not work since flask creates a "context" for everything to run (e.g. g, current_app etc.). The with_appcontext decorator adds this context before running the init_db_command
@click.command('initdb', help="initialise the database") # If we run "flask initdb", this function will run.
@with_appcontext
def init_db_command():
    init_db()
    click.echo('DB initialised') # This the click library API to print a message on the screen


# All commands and other things need to be registered into the
# application. We write a function here that can be called inside
# __init__.py which will add the init_db_command to the CLI. If you
# run flask --help now, you will see the initidb command there. Also,
# we add a "hook" to automatically call close_db when the app finishes
# execution. This will make sure that database connections are closed
# when done.
def init_app(app):
    app.teardown_appcontext(close_db) #hook
    app.cli.add_command(init_db_command)

