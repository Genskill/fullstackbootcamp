from flask import Flask

def create_app(): # This name is special
    app = Flask("jobs")
    app.config.from_mapping(
        SECRET_KEY = 'ucv1g.LGN1pss',
        DATABASE = 'naukri'
    )

    @app.route("/")
    def index():
        return "Hello"

    from . import jobs
    app.register_blueprint(jobs.bp)

    return app
    
        
