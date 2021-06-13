import psycopg2
from flask import Flask, request
from flask import render_template, jsonify


name = "default"

app = Flask("Job site")

items = ["python", "perl", "ruby"]

dbconn = psycopg2.connect("dbname=naukri")

@app.route("/api")
def api():
    print(request.headers)
    if request.headers.get("appId") != "109":
        return jsonify({"Error" : "Need appId to work"})
    else:
        x = {"name" : name, "language" : "python"}
        return jsonify(x)

@app.route("/") 
def index():
    cursor = dbconn.cursor()
    cursor.execute("select count(*) from openings")   # Query
    count_of_jobs = cursor.fetchall()[0][0]  # Get data
    return render_template("main.html", njobs=count_of_jobs) # Render


@app.route("/jobs") # decorator
def jobs():
    cursor = dbconn.cursor()
    cursor.execute("select title, company_name, jd_text from openings") # Query
    jobs = cursor.fetchall() # Get data
    return render_template("jobslist.html", jobs = jobs) #Render


if __name__ == "__main__":
    import sys
    name = sys.argv[1]
    app.run(debug=True)
