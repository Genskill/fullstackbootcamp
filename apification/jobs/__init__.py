import  random
from flask import Flask, render_template

# create_app is a function which will automatically called by the
# flask command line program create an instance of the application.
#
# The app is always the same. However, we might want it run on a
# different database for testing. This ability to call a function to
# create an app allows to manage this easily.
def create_app():
    app = Flask("jobs")

    # The config contains parameters (like db connection, perhaps some
    # secret keys and things like that. We're loading the config
    # directly from a mapping (dict like object). However, there are
    # other ways to load config (and usually, we load them from
    # files. You can refer to
    # https://flask.palletsprojects.com/en/2.0.x/config/ to understand
    # different ways of loading files.
    # 
    # There is no one single way to do this. There are multiple ways
    # to do it since there are multiple setups possible.
    app.config.from_mapping(
        DATABASE="naukri"
    )
    
    # Flask apps can either be written with all the URLs, code, db
    # etc. everything in a single file. This will make it very hard to
    # manage. Creating blueprints allows us to create "mini
    # applications" which can be all pulled together by the main
    # application to create the whole app. Blueprints can also share
    # code so that duplication is limited.  Refer to
    # https://flask.palletsprojects.com/en/2.0.x/blueprints/

    # We create the application as a python package. This page
    # describes how it works.
    # https://docs.python.org/3/tutorial/modules.html#packages. We
    # import the jobs module in this package and then register the
    # blueprint we've created in there into the main application
    # thereby adding all the URLs defined inside jobs to the main app.

    from . import jobs 
    app.register_blueprint(jobs.bp)

    from . import db 
    db.init_app(app) # This is where we're registering everything when
                     # a new application is created. This will add the
                     # commands we created to the command line and the
                     # hook to close database connections when we're
                     # done.


    # This is a small function to serve a random quote when we go the main page (/). Keeping it empty is ugly
    @app.route("/")
    def index():
        quotes = [["The best way to get started is to quit talking and begin doing.", "Walt Disney"],
                  ["The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.", "Winston Churchill"],
                  ["Don’t let yesterday take up too much of today.", "Will Rogers"]]
        quote, author = random.choice(quotes)
        conn = db.get_db()
        curs = conn.cursor()
        curs.execute("select count(*) from openings")
        count = curs.fetchone()[0]
        curs.execute("select crawled_on from crawl_status order by crawled_on desc limit 1");
        crawl_date = curs.fetchone()[0]

        return render_template('index.html', quote=quote, author=author, count=count, date = crawl_date)


    from . import crawler
    crawler.init_app(app)

    return app
    
