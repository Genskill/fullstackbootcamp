import csv
import sys

import psycopg2

def dump(fname):
    dbconn = psycopg2.connect("dbname=superhero")
    cursor = dbconn.cursor()
    f = open(fname, "w")
    writer = csv.writer(f)

    cursor.execute("SELECT name, gender from heroes where gender='m'");
    for name, gender in cursor.fetchall():
        writer.writerow([name,gender])

    dbconn.commit()
    
    f.close()
    

def main():
    fname  =sys.argv[1]
    dump(fname)

main()
    
