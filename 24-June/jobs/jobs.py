# This is the jobs part of the application. Our actual code for the
# jobs related parts are going to be in this file.  We'll be using the
# Blueprint just like a regular Flask app (with .route etc.)
from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
# g is an object that can store other objects throughout your
# application. If there's some part of the code that needs to do
# something and make that something available to all other parts of
# the application, it can simply put it inside g and it will become
# visible to the rest of the app. g stands for global. More
# information here
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.g and
# https://flask.palletsprojects.com/en/2.0.x/appcontext/
from flask import g

# This module contains all the code and functions necessary for
# database related operations
from . import db

# The is the Blueprint creation. the first 2 arguments are the name of
# the Blueprint. The second argument is the __name__ of the Blueprint
# which will be used in things like the logger etc.
# https://flask.palletsprojects.com/en/2.0.x/blueprints/ has more
# information. The url_prefix says that all the URLs below will have
# /jobs prepended to them.
bp = Blueprint("jobs", "jobs", url_prefix="/jobs")

@bp.route("/")
def alljobs():
    conn = db.get_db() # Notice how we use the function from the db
                       # module to get the database connection.
    cursor = conn.cursor()
    cursor.execute("select o.id, o.title, o.company_name, s.name from openings o, job_status s where s.id = o.status order by s.name") # Query
    jobs = cursor.fetchall() # Get data

    # one extra query here to find out when the last crawl was done so that we can display it in the sidebar.
    cursor.execute("select crawled_on from crawl_status order by crawled_on desc limit 1");
    crawl_date = cursor.fetchone()[0]

    if (request.accept_mimetypes.best == "application/json"):
        return jsonify(dict(jobs = [dict(id = id, title=title) for id, title, _, _ in jobs]))
    else:
        return render_template("jobs/jobslist.html", jobs = jobs, count=len(jobs), date=crawl_date) # Render the data using the jobs/jobslist template.

# The <> inside the URL specifies variable part of the URL. If the URL
# was /test/here, it will match only exactly /test/here. If you give
# the URL as /test/<here>, it will match anything that starts with
# /test/ (e.g. /test/me, /test/it, /test/there etc.) and the extra
# part will there in the variable "here" and will be passed to the
# function. In this case, we can get the job id we're specifically
# interested in using URLs /jobs/123, /jobs/432 etc.
@bp.route("/<jid>") 
def jobdetail(jid):
    conn = db.get_db()
    cursor = conn.cursor()
    # We fetch additional information including the status of this job and the crawl date with this query
    cursor.execute("select o.title, o.company_name, s.name, o.jd_text, o.crawled_on from openings o, job_status s where o.id = %s and s.id = o.status", (jid,))
    job = cursor.fetchone()
    if not job:
        # If the job is not found, we return the job details page
        # without any parameters. Hence the {%if title%} test will
        # fail and the {%else%} part will be executed. The 404
        # indicates the HTTP status code. 404 stands for "page not
        # found"
        if (request.accept_mimetypes.best == "application/json"):
            return jsonify({"error": f"No job with id {jid}"})
        else:
            return render_template("jobs/jobdetails.html"), 404


    title, company, status, info, crawled_on = job
    jid = int(jid)
    if jid == 1:
        prev = None
    else:
        prev = jid - 1
    nxt = jid + 1

    # This dictionary is used to decide the colour and look of the
    # various statuses. It maps from the name of the status in our
    # database to the corresponding css class. This could have been in
    # the database itself as well.
    classes = {"crawled": "primary",
               "applied" : "secondary",
               "ignored" : "dark",
               "selected" : "success",
               "rejected" : "danger"}
    if (request.accept_mimetypes.best == "application/json"):
        ret = dict(id = jid,
                   jd = info,
                   title = title,
                   company = company,
                   status = status,
                   crawled_on = str(crawled_on))
        return jsonify(ret)
    else:
        return render_template("jobs/jobdetails.html", 
                               jid = jid,
                               info = info, 
                               nxt=nxt, 
                               prev=prev, 
                               title = title, 
                               company=company, 
                               status=status, 
                               cls=classes[status], 
                               crawled_on=crawled_on)



@bp.route("/<jid>/edit", methods=["GET", "POST",])
def edit_job(jid): 
    conn = db.get_db()
    cursor = conn.cursor()
    # We fetch additional information including the status of this job and the crawl date with this query
    cursor.execute("select o.title, o.company_name, s.name, o.jd_text, o.crawled_on from openings o, job_status s where o.id = %s and s.id = o.status", (jid,))
    job = cursor.fetchone()
    if not job:
        return render_template("jobs/jobdetails.html"), 404    

    if request.method == "GET":
        title, company_name, status, jd, crawled_on = job
        cursor.execute("select id,name from job_status")
        statuses = cursor.fetchall()
        return render_template("jobs/jobedit.html", 
                               jid = jid,
                               info=jd,
                               statuses = statuses,
                               status = status,
                               title = title, 
                               crawled_on = crawled_on)
    elif request.method == "POST":
        status = request.form.get("status")
        jd = request.form.get("jd")
        cursor.execute("update openings set jd_text = %s, status=%s where id=%s", (jd, status, jid))
        conn.commit()
        return redirect(url_for("jobs.jobdetail", jid=jid), 302)





