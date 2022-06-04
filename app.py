from flask import Flask, render_template, send_from_directory
from os import path, walk

from routes_list import routes_list
from config import Config

app = Flask(__name__, static_url_path=f"{Config.APP_PREFIX}/static")
print(app.static_url_path)
app.config.from_object(Config)
app_prefix = Config.APP_PREFIX

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
@app.route("/<path>")
@app.route("/<path>/")
@app.route(f"/{app_prefix}/<path>")
@app.route(f"/{app_prefix}/<path>/")
@app.route(f"/<path:path>")
def route_configured(path="/"):
	cssList,jsList = get_static_files()
	seo_data = {
		"title": "Marketplace",
		"description": "wholesale marketplace sapcozgut"
	}

	for r in routes_list:
		if r["path"] == path:
			seo_data["title"] = r["title"]
			seo_data["description"] = r["description"]

	return render_template('index.html',
		seo_data = seo_data,
		cssList = cssList,
		jsList = jsList,
		logo_filename = Config.LOGO_IMAGE_FILENAME,
		app_prefix = app_prefix,
	)

@app.route("/locales/<lang>/<filename>")
def get_locale_file(lang, filename):
	return send_from_directory('static', f'locales/{lang}/{filename}')


app_port = int(Config.APP_PORT) if Config.APP_PORT else 5000
app_host = Config.APP_HOST or "0.0.0.0"

if __name__ == "__main__":
	app.run(host=app_host, port=app_port, threaded=True)