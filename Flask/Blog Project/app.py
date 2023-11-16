from flask import Flask, request, render_template
 
app = Flask(__name__)

leaderboard_list=[
    {'username':'Baodan', 'grade':95, 'age':16},
    {'username':'Ethan', 'grade':0, 'age':13},
    {'username':'Celina', 'grade':99, 'age':11},
    {'username':'Angeline', 'grade':96, 'age':15},
]

@app.route('/leaderboard')
def leaderboard():
    return render_template('student.html', leaderboard=leaderboard_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
