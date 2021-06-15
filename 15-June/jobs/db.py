import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(f"dbname={current_app.config['DATABASE']}")
    return g.db

def close_db():
    if 'db' in g:
        g.db.close()
        g.pop('db')

# Can add the crawler functions here if necessary. Try it as homework 
# https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
        
