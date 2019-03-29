from flask import Flask, render_template
from mlab import river_collection
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/river')
def river():
    river_list = river_collection.find()
    return render_template('river.html',all_river = river_list)
@app.route('/river/length')
def river2():
    river_length = river_collection.find({"continent" : "S. America"})
    return render_template('length.html',all_america = river_length)
    

if __name__ == '__main__':
  app.run(debug=True)
