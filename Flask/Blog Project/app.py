from flask import Flask, request, render_template
 
app = Flask(__name__)

leaderboard_list=[
    {'username':'Baodan', 'grade':69, 'age':78, 'city':'Nampa'},
    {'username':'Ethan', 'grade':-100000000, 'age':1, 'city':'Huntsville'},
    {'username':'Celina', 'grade':99, 'age':11, 'city':'Albuquerque'},
    {'username':'Angeline', 'grade':96, 'age':45, 'city':'Meridian'},
]

@app.route('/leaderboard')
def leaderboard():
    return render_template('student.html', leaderboard=leaderboard_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
