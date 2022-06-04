import sys
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath('.')
load_dotenv(path.join(basedir, '.env'))

class Config:
	# get OS Type to configure app for Windows or Linux
	OS_TYPE = sys.platform
	APP_BASEDIR = path.abspath('.')

	APP_PORT = int(environ.get('APP_PORT')) if environ.get('APP_PORT') else 5000
	APP_HOST = environ.get('APP_HOST') or "0.0.0.0"

	# basic app configs (required)
	SECRET_KEY = environ.get('SECRET_KEY')