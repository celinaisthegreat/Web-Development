from flask import Flask, request, render_template
# Flask is used to make a new flask app
# request is used to get or post something on an application
# render_template renders/shows an html page on a particular url/link

# making a flask app  
app = Flask(__name__)

questions=[
    {
            "question" : "Is Ethan from the Goofy family?",
            "option" : ["No","Yes","Idk","Goofy"],
            "correct_option" : "Yes"
    },
    {
            "question" : "Is Ethan sus?",
            "option" : ["Of course","Yes","No","Goofy"],
            "correct_option" : "Of course"
    },
    {
            "question" : "Is Ethan not the best?",
            "option" : ["No","True","YESSSSSSSSS","Goofy"],
            "correct_option" : "True"
    }
]

score = 0

current_question= 0

@app.route('/')
def index():
    return "Welcome to the quiz application!"

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score
    global current_question
    if request.method == "POST":
        user_answer = request.form.get('answer')
        correct_answer = questions[current_question]["correct_option"]
        if user_answer == correct_answer:
            score += 1
        current_question += 1
        if current_question < len(questions):
            return render_template("quiz.html", question = questions[current_question]["question"],
                                   options=questions[current_question]["option"])

        else:
            feedback = f"You scored {score}/{len(questions)}. )"
            score = 0
            current_question = 0
            return render_template("result.html", feedback=feedback)

    return render_template("quiz.html", question = questions[current_question]["question"],options=questions[current_question]["option"])         

if __name__ == "__main__":
    app.run(debug=True)