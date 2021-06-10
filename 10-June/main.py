import psycopg2
from flask import Flask, request


app = Flask("Job site")

items = ["python", "perl", "ruby"]

dbconn = psycopg2.connect("dbname=naukri")

@app.route("/") 
def index():
    cursor = dbconn.cursor()
    cursor.execute("select count(*) from openings")
    njobs = cursor.fetchall()[0][0]
    
    return f"""
    <html>
    <head>
    <title> Jobs page </title>
    </head>

    <body>
    <h1>Welcome to the jobs page</h1>
    There are currently <a href="/jobs">{njobs}</a> jobs
    </body>
    </html>
    """


@app.route("/jobs") # decorator
def jobs():
    cursor = dbconn.cursor()
    cursor.execute("select title, company_name, jd_text from openings")
    ret = []


    for title, company_name, jd in cursor.fetchall():
        item = f"<li>{title} :: {company_name} <br/> {jd}</li>"
        ret.append(item)
    jobs = "".join(ret)

    return f"""
    <html>
    <head>
    <title> Jobs page </title>
    </head>

    <body>
    <h1>Welcome to the jobs page</h1>
    <ol>
    {jobs}
    </ol>
    </body>
    </html>
    """



    return f"""List of jobs is:

    {l}"""

# http://127.0.0.1/add?item=x
@app.route("/add")
def add_item():
    item = request.args.get("item")
    items.append(item)
    return f"No. of items is now {len(items)}"


# https://flask.palletsprojects.com/en/2.0.x/
