from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
        "nhat" : {
            "name" : "Nguyễn Quang Nhật",
            "age" : 21,
            "gender" : "male",
            "hobbies" : "football"
        },
        "duc" : {
            "name" : "Phạm Minh Đức",
            "age" : 21,
            "gender" : "male",
            "hobbies" : "gái"
        },
        "tung" : {
            "name" : "Trần Công Tùng",
            "age" : 21,
            "gender" : "male",
            "hobbies" : "auto chess"
        },
        "huyanh" : {
            "name" : "Nguyễn Huy Anh",
            "age" : 21,
            "gender" : "male",
            "hobbies" : "gái"
        }
    }
    if username in users :
        return render_template('user.html',users=users[username])
    else :
        return "User not found" 

if __name__ == '__main__':
  app.run( debug=True)
