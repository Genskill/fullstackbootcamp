import datetime
import sys

import click 
import requests
import bs4
from flask.cli import with_appcontext

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

    # These two statements get the id for the "crawled" status. When
    # we crawl first, we set the status of all the jobs to "crawled"
    cursor.execute("select id from job_status where name = 'crawled'");
    crawled_id = cursor.fetchone()[0]
    
    crawled_on = datetime.date.today() # We also find today's date to keep track of when we crawled the job
    for i in jobs:
        title = i['title']
        job_id = i['jobId']
        company_name = i['companyName']
        jd_url = i['jdURL']
        soup = bs4.BeautifulSoup(i['jobDescription'], features="html.parser")
        jd = str(soup.text)
        cursor.execute("""INSERT INTO
        openings (title, job_id, company_name, jd_url, jd_text, status, crawled_on) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",(title, job_id, company_name, jd_url, jd, crawled_id, crawled_on))
    click.echo(f"Added {len(jobs)} jobs.")

    # We keep track of a separate crawled on to find the last date of
    # crawl and store this in a separate table called crawled on
    crawled_on = datetime.datetime.now()
    cursor.execute("insert into crawl_status (crawled_on) values (%s)", (crawled_on,));
    dbconn.commit()

@click.command('crawl', help="Crawl for jobs") # If we run "flask crawl", this function will run.
@with_appcontext
def crawl_command():
    jobs = fetch_jobs()
    insert_jobs(jobs)    

def init_app(app):
    app.cli.add_command(crawl_command)
    

