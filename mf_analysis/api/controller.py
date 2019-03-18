'''Controllers used by AR PoC Server'''
import os

from flask import Flask, request, render_template

ROOT_DIR = "/Users/1021839/fun/github/mf-analysis/"

APP = Flask(__name__, template_folder='../../templates/')
APP.config['UPLOAD_FOLDER'] = ROOT_DIR + "data/upload/"
APP.config['AMFI_SCRAPE_FOLDER'] = ROOT_DIR + "data/amfiindia/"
APP.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@APP.route("/")
def hello():
    '''Hello Controller'''
    return "Hello World"


@APP.route("/upload-insights")
def upload_insights():
    return render_template('frontend/src/upload-insights.html')


@APP.route("/upload", methods=['POST'])
def upload():
    file = request.files['insight-file']
    filename = "insights.csv"
    file.save(os.path.join(APP.config['UPLOAD_FOLDER'], filename))
    return "OK"


if __name__ == "__main__":
    APP.run()
