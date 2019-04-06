from flask import Flask , render_template , redirect , request , session
from bikedatabase import bike_collection
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/new_bike', methods = ["GET" , "POST"])
def rental():
    if request.method == "GET":
        return render_template('bikerental.html')
    elif request.method == "POST":
        form = request.form 
        bike_model = form["input_model"]
        bike_fee = form["input_fee"]
        bike_image = form["input_image"]
        bike_year = form["input_year"]
        print(form)
        bikes = {
            "model" : bike_model,
            "fee" : bike_fee,
            "image" : bike_image,
            "year" : bike_year
        }
        bike_collection.insert_one(bikes)
        return redirect('/new_bike')


if __name__ == '__main__':
  app.run(debug=True)
 