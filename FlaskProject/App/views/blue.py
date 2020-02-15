from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from flask_mail import Message
from App.ext import db, mail, cache
from App.models import User
from App.utils import send_verify_code
from ..static.py.os_status import Computer
import time

# 蓝图定义
blue = Blueprint("blue", __name__, static_folder="../templates")

# 系统信息
@blue.route('/')
def sys_status():
    computer = Computer()
    service_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return render_template("base.html",
                           c_name=computer.name,
                           c_ip=computer.ip,
                           c_adress=computer.adress,
                           c_os_version=computer.os_version,
                           c_cpu=computer.cpu,
                           c_cpu_sum=computer.cpu_sum,
                           c_start_up=computer.startup,
                           c_runtime=computer.runtime,
                           c_disk_info=computer.disk_info,
                           service_time=service_time,config=current_app.config)

# 注册
@blue.route('/user/register/',methods=['GET','POST'])
def user_register():
    # GET请求进入注册页面
    if request.method == 'GET':
        return render_template('register.html')
    # 在注册页面中进行POST请求
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        mobile = request.form.get('mobile')
        verifycode = request.form.get('verifycode')

        if verifycode != cache.get(username):
            return "Register failure!"
        # 实例化表对象
        user = User()
        user.name = username
        user.password = password
        user.mobile = mobile
        # 添加数据并提交至数据库
        db.session.add(user)
        db.session.commit()
        # 注册成功提示
        return "Register success!"

# 登录
@blue.route('/user/login/',methods=['GET','POST'])
def user_login():
    # GET请求进入登录页面
    if request.method == 'GET':
        return render_template('login.html')
    # 在登录页面中进行POST请求
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 实例化表对象
        user = User.query.filter(User.name.__eq__(username)).first()
        # 判断hash密码的正确性
        if user and user.check_password(password):
            # 登录成功提示
            return "Login success!"
        else:
            # <SecureCookieSession {'_flashes': [('message', '账号或密码错误！')]}>
            flash("账号或密码错误！")
            # 登录失败重定向到当前页面并输出提示
            return redirect(url_for('blue.user_login'))

# 发送邮件
@blue.route('/send_email/')
def send_email():
    message = Message("标题内容", recipients=["mskyvip@163.com",])
    message.body = '普通文本'
    message.html = "html"
    mail.send(message=message)
    return "Email send success!"

# 发送验证码
@blue.route('/send_code/')
def send_code():
    username = request.args.get('username')
    mobile = request.args.get('mobile')
    resp = send_verify_code(mobile)
    result = resp.json()

    print(result)
    if result.get('code') == 200:
        obj = result.get('obj')
        cache.set(username, obj)
        data = {
            'msg': 'success',
            'status': 200
        }
        return  data

    data = {
        'msg': 'failure',
        'status':400
    }
    return data