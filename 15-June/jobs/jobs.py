import functools

from flask import Blueprint, render_template

from jobs.db import get_db

bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@bp.route("/")
def all_jobs():
    db = get_db()
    c = db.cursor()
    c.execute("select title, company_name, jd_text from openings") # Query
    jobs = c.fetchall() # Get data
    c.close()
    return render_template("jobs/jobslist.html", title = "My Jobs", jobs = jobs) #Render


