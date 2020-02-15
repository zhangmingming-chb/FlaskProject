from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app
import os

# 从环境变量中获取环境配置
# develop:开发环境
# staging:演示环境
# product:生产环境
# testing:测试环境
# default:默认环境
env = os.environ.get('FLASK_ENV','product')

# 创建初始化插件和配置后的app对象
app = create_app(env)

# 将app传入Manager中创建manager对象
manager = Manager(app=app)

# 将数据库模型的迁移命令添加至manager对象中
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    # 运行manager
    manager.run()
