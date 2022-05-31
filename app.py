from logging import debug
from flask import Flask
from flask import render_template
from flask import send_from_directory

import routes_list

app = Flask(__name__)


from os import listdir, path, walk
from dotenv import load_dotenv

def get_static_files():
  basedir = path.abspath('.')
  staticDir = path.join(basedir,'static')
  cssList,jsList = [], []

  for (root, dirs, file) in walk(staticDir):
    for f in file:
      if ('.css' in f or '.js' in f) and not ('.json' in f or '.map' in f or '.chunk' in f or '.txt' in f):
        if ('.css' in f):
          filedir = root.split(basedir)[1]
          fulldir = path.join(filedir, f)
          cssList.append(fulldir)
        if ('.js' in f):
          filedir = root.split(basedir)[1]
          fulldir = path.join(filedir, f)
          jsList.append(fulldir)
  return cssList,jsList

@app.route("/")
def index():
  cssList,jsList = get_static_files()
  seo_data = {
    "title": "Marketplace",
    "description": "wholesale marketplace saphasap"
  }
  return render_template('index.html',
    seo_data = seo_data,
    cssList = cssList,
    jsList = jsList)


@app.route("/<route>")
def route_configured(route):
  cssList,jsList = get_static_files()
  seo_data = {
    "title": "blank title",
    "description": "Blank desc",
  }

  for r in routes_list:
    if r["path"] == route:
      seo_data["title"] = r["title"]
      seo_data["description"] = r["description"]

  return render_template('index.html',
    seo_data = seo_data,
    cssList = cssList,
    jsList = jsList)

@app.route("/locales/<lang>/<filename>")
def get_locale_file(lang, filename):
  return send_from_directory('static', f'locales/{lang}/{filename}')


if __name__ == "__main__":
  app.run("0.0.0.0", port=5000, debug=True)
