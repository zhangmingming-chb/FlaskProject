# 此文件用于定义中间件
from flask import request

def load_middleware(app):

    @app.before_request
    def before():
        """
        before_request一般用途:
                        统计
                        优先级
                        反爬虫
                        用户认证
                        用户权限
        """
        print("请求报文处理之前，执行该函数")
        print(request.url)


    @app.after_request
    def after(res):
        """
        after_request一般用途:
                        响应报文的处理
        """
        print("请求报文处理完成之后，返回响应报文之前，执行该函数")
        print(type(res))
        print(res)

        return res # 必须返回一个<class 'flask.wrappers.Response'>类型
