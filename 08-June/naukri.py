import requests
import bs4
import psycopg2

import sys



def fetch_jobs():
    url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
    headers={"appid" : "109",
             "systemid" : "109"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data['jobDetails']

def insert_jobs(jobs):
    # title   
    # jobId   
    # companyName   
    # x tagsAndSkills   
    # x placeholders   
    # jdURL   
    # jobDescription   
    for i in jobs:
        soup = bs4.BeautifulSoup(i['jobDescription'])
        f = open(str(jobid)+".txt", "w")

def create_db():
    dbconn = psycopg2.connect("dbname=naukri")
    cursor = dbconn.cursor()
    f= open("jobs.sql")
    sql_code = f.read()
    f.close()
    cursor.execute(sql_code)
    dbconn.commit()

def main(arg):
    if arg == "create":
        create_db()
    elif arg == "crawl":
        jobs = fetch_jobs()
        insert_jobs(jobs)
    else:
        print (f"Unknown command {arg}")
    
if __name__ == "__main__": #import guard
    main(sys.argv[1])

