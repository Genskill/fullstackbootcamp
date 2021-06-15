import functools

from flask import Blueprint

from jobs.db import get_db
bp = Blueprint('jobs', __name__, url_prefix='/jobs')


bp.route("/")
def all_jobs():
    db = get_db()
    db.execute("select title, company_name, jd_text from openings") # Query
    jobs = cursor.fetchall() # Get data
    return render_template("jobs/jobslist.html", jobs = jobs) #Render

