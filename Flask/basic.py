# isUppercase = False
# isNumbers = False
# isSymbols = False

# isUppercase = bool(input("Do you want uppercase letters? "))
# isNumbers = bool(input("Do you want numbers? "))
# isSymbols = bool(input("Do you want symbols? "))
# length = int(input("How many characters do you want?"))

# import random
# def generate_password():
#     choices = list("abcdefghijklmnopqrstuvwxyz")

#     if isUppercase == True:
#         choices.extend("ABCDEFGHIJKLMOPQRSTUVWXYZ")
#     if isNumbers == True:
#         choices.extend("0123456789")
#     if isSymbols == True:
#         choices.extend('''"'[]|\~!@#{}$/%^&*()_-+=<>,.:;?''')

#     mypassword = ""
#     for i in range(length):
#         mypassword += random.choice(choices)

#     print(mypassword)
# generate_password()

import random
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

if __name__=="__main__":
    app.run()


































