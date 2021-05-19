# Scraping

## Getting your environment setup
1. Install `virtualenv`. You can install the virtualenv tool using
   `sudo apt-get install python3-virtualenv` (on Ubuntu)

2. Create a virtual environment using
   `virtualenv -p /usr/bin/python3 /tmp/mscraper` 
   You can change the location of your virtualenv. I've used
   `/tmp/mscraper` as an example.
   
3. Then activate the virtualenv using
   `. /tmp/mscraper/bin/activate`. You can deactivate it by typing
   `deactivate` and hitting enter. Don't forget the initial `.` in the
   invocation to activate.

## Installing packages
1. After activating your virtualenv, use `pip install requests` to install the requests library.
2. Then do `pip install beautifulsoup4` to install Beautiful Soup. 
3. Alternatively, you can simply run `pip install -r requirements.txt` to install both of them in one shot. When we manage large projects, we usually provide a `requirements` file as part of the package.

## Running scraper
3. Then you will be able to run the `scraper.py` program to scrape metrolyrics.com

   
