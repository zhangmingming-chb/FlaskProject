# 配置插件
# from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_caching import Cache
# 创建插件对象
# session = Session()
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
cache = Cache(config={
    'CACHE_TYPE':'simple'
})
mail = Mail()


# 初始化函数
def init_extension(app):
    # 初始化会话插件
    # 使用flask-session插件会和flash()有冲突
    # session.init_app(app)
    # 初始化模型插件
    db.init_app(app)
    # 初始化迁移插件
    migrate.init_app(app,db)
    # 初始化bootstrap插件
    bootstrap.init_app(app)
    # 初始化debugtoolbar插件
    DebugToolbarExtension(app)
    # 初始化邮箱插件
    cache.init_app(app)
    # 初始化邮箱插件
    mail.init_app(app)