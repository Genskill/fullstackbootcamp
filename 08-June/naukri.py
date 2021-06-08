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
    # x tagsAndSkills   
    # x placeholders   
    dbconn = psycopg2.connect("dbname=naukri")
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
    dbconn.commit()

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

