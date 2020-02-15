# 配置文件
import datetime


def get_db_uri(database_info):
    engine   = database_info.get('ENGINE')   or 'sqlite'
    driver   = database_info.get('DRIVER')   or ''
    user     = database_info.get('USER')     or ''
    password = database_info.get('PASSWORD') or ''
    host     = database_info.get('HOST')     or ''
    port     = database_info.get('PORT')     or ''
    db       = database_info.get('DB')       or 'sqlite.db'

    return  '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, db)

class Config:
    """
    配置对象
    """
    # 调试模式
    DEBUG = False
    # 测试模式
    TESTING = False
    # 追踪对象的修改并发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置秘钥
    SECRET_KEY = 'adwafawidnawdaw1ednabc'
    # session过期时间配置
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=16)

    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    MAIL_USERNAME = "mskyvip@163.com"
    MAIL_PASSWORD = "zhangjiming123"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopConfig(Config):
    """
    开发环境
    """
    ENV = 'development'
    DEBUG =  True
    DB_INFO = {
        'ENGINE'  :'mysql',
        'DRIVER'  :'pymysql',
        'USER'    :'root',
        'PASSWORD':'zhangjiming123.',
        'HOST'    :'182.61.18.124',
        'PORT'    :'3306',
        'DB'      :'db1'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DB_INFO)

class TestConfig(Config):
    """
    测试环境
    """
    ENV = 'testing'
    TESTING =  True
    DB_INFO = {
        'ENGINE'  :'mysql',
        'DRIVER'  :'pymysql',
        'USER'    :'root',
        'PASSWORD':'zhangjiming123.',
        'HOST'    :'182.61.18.124',
        'PORT'    :'3306',
        'DB'      :'db1'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DB_INFO)


class StagingConfig(Config):
    """
    演示环境
    """
    ENV = 'staging'
    DB_INFO = {
        'ENGINE'  :'mysql',
        'DRIVER'  :'pymysql',
        'USER'    :'root',
        'PASSWORD':'zhangjiming123.',
        'HOST'    :'182.61.18.124',
        'PORT'    :'3306',
        'DB'      :'db1'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DB_INFO)

class ProductConfig(Config):
    """
    生产环境
    """
    ENV = 'production'
    DB_INFO = {
        'ENGINE'  :'mysql',
        'DRIVER'  :'pymysql',
        'USER'    :'root',
        'PASSWORD':'zhangjiming123.',
        'HOST'    :'182.61.18.124',
        'PORT'    :'3306',
        'DB'      :'db1'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DB_INFO)

envs = {
        'develop':DevelopConfig,
        'testing':TestConfig,
        'staging':StagingConfig,
        'product':ProductConfig,
        'default':DevelopConfig
        }
