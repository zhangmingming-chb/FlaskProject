from flask import Flask
from App.middleware import load_middleware
from App.views import init_view
from App.ext import init_extension
from App.settings import envs

def create_app(env):
    # 创建app对象
    app = Flask(__name__)
    # 获取settins.py文件中的配置对象
    app.config.from_object(envs.get(env))
    # 初始化插件
    init_extension(app)
    # 初始化视图
    init_view(app)
    # 加载中间件
    load_middleware(app)

    return app

