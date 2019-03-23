from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight,height):
    heightcm = height/100
    bmi = round(weight/(heightcm*heightcm),2)
   
    if (bmi < 16) : 
        bmi = ("BMI của bạn là : "+str(bmi) + " You are Severely underweight")
    elif (16 <= bmi < 18.5): 
        bmi = ("BMI của bạn là : "+str(bmi) + " You are Underweight")
    elif (18.5 <= bmi < 25): 
        bmi = ("BMI của bạn là : "+str(bmi) + " You are Normal")
    elif (25 <= bmi < 30): 
        bmi = ("BMI của bạn là : "+str(bmi) + " You are Overweight")
    elif (bmi > 30): 
        bmi = ("BMI của bạn là : "+str(bmi) + " You are Obese")
    return bmi 
    
if __name__ == '__main__':
  app.run( debug=True)
 