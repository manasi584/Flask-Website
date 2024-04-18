from flask import Flask,render_template,jsonify

app = Flask(__name__)

COURSE=[
  {
    'id':1,
    'title':'Data Analysis',
    'location':'Online',
  },
  {
    'id':2,
    'title':'Fundamentals of Options Trading',
    'location':'Offline - New Delhi'
    
  },
  {
    'id':3,
    'title':'Indian Economy -A Case Study',
    'location':'Hybrid'
  }
]


@app.route("/")
def hello_world():
    return render_template('home.html',course=COURSE,company="InvestLearn")

#creating a json end point instead of html
@app.route("/courses")
def courses():
  return jsonify(COURSE)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)