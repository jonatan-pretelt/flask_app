import os

class Config(object):
	SECRET_KEY =  os.environ.get('SECRET_KEY') or '95dc968aabd4f95c1501a03f11da72ae'

	MONGODB_SETTINGS = {'db' : 'UTA_Enrollment'}