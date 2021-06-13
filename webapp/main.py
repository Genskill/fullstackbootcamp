# main.py
from flask import Flask, request, render_template

import estimators

app = Flask("Genskill")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/estimate", methods=["POST"])
def estimate():
    algorithm = request.form['algorithm']
    iterations = request.form['iterations']
    if algorithm == "mc":
        estimate = estimators.estimate_mc(int(iterations))
    elif algorithm == "wallis":
        estimate = estimators.estimate_wallis(int(iterations))

    names = {"mc" : "Monte Carlo Estimation",
             "wallis" : "Wallis product estimation"}
    return render_template("estimate.html",
                           algorithm = names[algorithm],
                           iters = iterations,
                           estimate = estimate)



if __name__ == "__main__":
    app.run()
