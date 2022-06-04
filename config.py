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

	LOGO_IMAGE_FILENAME = environ.get('LOGO_IMAGE_FILENAME') or "logo_black.png"
	COMPANY_NAME = environ.get('COMPANY_NAME') or "Marketplace"
	COMPANY_URL = environ.get('COMPANY_URL') or "https://saphasap.com"
	APP_PREFIX = environ.get('APP_PREFIX') or ""

	# basic app configs (required)
	SECRET_KEY = environ.get('SECRET_KEY')