import sys

import click 
from flask.cli import with_appcontext
import requests
import bs4

from . import db

def fetch_jobs():
    url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
    headers={"appid" : "109",
             "systemid" : "109"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data['jobDetails']

def insert_jobs(jobs):
    dbconn = db.get_db()
    cursor = dbconn.cursor()
    for i in jobs:
        title = i['title']
        job_id = i['jobId']
        company_name = i['companyName']
        jd_url = i['jdURL']
        soup = bs4.BeautifulSoup(i['jobDescription'], features="html.parser")
        jd = str(soup.text)
        cursor.execute("""INSERT INTO
        openings (title, job_id, company_name, jd_url, jd_text) 
        VALUES (%s, %s, %s, %s, %s)""",(title, job_id, company_name, jd_url, jd))
    click.echo(f"Added {len(jobs)} jobs.")
    dbconn.commit()

@click.command('crawl', help="Crawl for jobs") # If we run "flask crawl", this function will run.
@with_appcontext
def crawl_command():
    jobs = fetch_jobs()
    insert_jobs(jobs)    

def init_app(app):
    app.cli.add_command(crawl_command)
    

