from flask import Flask, request, render_template, flash
from models import User
app = Flask(__name__)
app.secret_key="123"

@app.route('/')
def hello_world():
    content="hello word3"
    return  render_template("login.html",content=content)
#
# @app.route('/user',methods=["post"])
# def hello_user():
#     return "user hello"
# @app.route("/user/<id>")
# def userid(id):
#     return "hello user:"+id
# @app.route("/query_url")
# def query_url():
#     id =request.args.get("id")
#     return "hello user:"+id
@app.route("/one")
def one_index():
    return render_template("one_index.html")
@app.route("/two")
def two_index():
    return  render_template("two_index.html")
@app.route("/three")
def for_index():
    user = User(1,"张三")
    return  render_template("index.html",user=user)
@app.route("/login",methods=["POST"])
def login():


    form =request.form
    username =form.get('username')
    password =form.get('password')
    if not username:
        flash("请输入用户名")
        return render_template("login.html")
    if not password:
        flash("请输入密码")
        return render_template("login.html")
    if username=="admin" and password =="123456":
        flash("登陆成功")
        with open('list.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print("9888888888========", line)
        return render_template("one_index.html",lines=lines)
    else:
        flash("用户名或密码错误")
        return  render_template("login.html")
if __name__ == '__main__':
    print("99999999999999")
    app.run(debug=True,host='0.0.0.0',port=8080)
