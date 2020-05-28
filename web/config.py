import os
 
app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdb.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="lmarquesmoreira@techconfdb" #TODO: Update value
    POSTGRES_PW="P@ssw0rdLMM01"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm' 
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://nd081sbs.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=fd2hl9bwFNlGFlpdPqGWIWOV8h0jQjzzKhFm3uxnR0w=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='nd081-c3-notification-queue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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"'
    REDIS_PKEY = 'hiV87KBKhSxnRVHxY+EjTccbMHFr9O4CwrTkc+85Zqo='
    REDIS_HOST = 'nd081-c3-cache0001.redis.cache.windows.net'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False