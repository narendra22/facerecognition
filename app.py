
import os
from flask import Flask,request,render_template
from datetime import date
from datetime import datetime

#### Defining Flask App
app = Flask(__name__)


#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")




#### If these directories don't exist, create them
if not os.path.isdir('Attendance'):
    os.makedirs('Attendance')
if not os.path.isdir('static/faces'):
    os.makedirs('static/faces')
if f'Attendance-{datetoday}.csv' not in os.listdir('Attendance'):
    with open(f'Attendance/Attendance-{datetoday}.csv','w') as f:
        f.write('Name,Roll,Time,datetoday')




################## ROUTING FUNCTIONS #########################

@app.route("/")
@app.route("/index")
def index():  
    return render_template('index.html')
@app.route("/adds", methods=['GET', 'POST'])
def adds():
	return render_template("adds.html",datetoday2=datetoday2)

#### This function will run when we click on Take Attendance Button
@app.route('/start',methods=['GET'])
def start():
    if 'face_recognition_model.pkl' not in os.listdir('static'):
        return render_template('adds.html') 

  
       
    return render_template('result.html') 

@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
	return render_template("attendance.html")
#### This function will run when we add a new user
@app.route('/add',methods=['GET','POST'])
def add():   
    return render_template('adds.html') 
@app.route("/results", methods=['GET', 'POST'])
def results():
     return render_template('results.html')



@app.route("/login", methods=['GET', 'POST'])
def login():
	return render_template("login.html")
#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)