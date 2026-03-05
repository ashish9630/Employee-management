import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Ashish@9630'
    MYSQL_DB = 'leave_management'
    MYSQL_CURSORCLASS = 'DictCursor'
