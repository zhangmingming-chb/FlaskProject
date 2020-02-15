# 模型文件
from werkzeug.security import generate_password_hash, check_password_hash
from App.ext import db


class User(db.Model):
    # 自定义表名，默认表名为所在类名的小写
    # __tablename__ = "user_tb"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    password_hash = db.Column(db.String(256))
    mobile = db.Column(db.String(32), unique=True)

    @property
    def password(self):
        raise Exception("Error Action: Password can't be access")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.password_hash, value)

