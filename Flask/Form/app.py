from flask import Flask, render_template

# this makes a new flask application
app = Flask(__name__)

# this line makes a empty url which looks like 127.0.0.1.8080/
@app.route('/')
def index():# making a function to write the logic for the home page
    return render_template('index.html')# its showing index.html on the url mentioned

#as a single user can send multiple messages so we store it in a list of messages
messages[]

# it makes url 127.0.0.1.8080/submit and method POST means it is containing data 
# and its sending the data to the server
@app.route('/submit', methods=['POST'])
def submit()
    name = request.form["name"]# its taking the user input from the name field
    email = request.form["email"]# its taking the user input from the email field
    areyouacheeseburger = request.form["areyouacheeseburger"]# its taking the user input from the areyouacheeseburger field


if __name__ == '__main__':
    app.run()