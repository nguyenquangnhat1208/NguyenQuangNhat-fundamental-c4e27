from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "hello c4e27"
# @app.route('/say-hi/<name>')
# def sayhi(name):
#     return "hi " + name

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return str(a+b)
@app.route('/poem')
def poem():
    poems = [
        {
            "title" : "thơ con cóc",
            "content" : "Hôm nay trăng lên cao quá",
            "author" : "Huế",
            "gender" : "female"
        },
        {
            "title" : "thơ con gà",
            "content" : "Anh muốn hôn vào má",
            "author" : "Quân",
            "gender" : "male"
        }

    ]
  
    return render_template("poem.html",poems=poems)

if __name__ == '__main__':
  app.run(debug=True)
 