from flask import Flask, render_template
import this

app = Flask(__name__)

PROJECTS = [
  
  {
    'id': 1,
    'title': 'project1'
  },
  {
    'id': 2,
    'title': 'project2'
  },
  {
    'id': 3,
    'title': 'project3'
  }

]

@app.route("/")

def hello():
  return render_template('home.html', projects = PROJECTS, admName = 'Viktor')

if(__name__ == "__main__"):
  app.run(host = "0.0.0.0", debug = True)
  