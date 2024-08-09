from flask import Flask, render_template, session, jsonify, request
import random

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/index')
def index():
    list_of_num = range(1,50)
    return render_template("index.html", result=list_of_num)


@app.route('/start', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        range_start = int(request.form['start_number'])
        range_end = int(request.form['end_number'])
        list_of_num = range(range_start, range_end+1)
        server_number = random.choice(range(range_start, range_end+1))
        session['server_number'] = server_number
        return render_template("index.html", result=list_of_num)
    else:
        return render_template("index.html")

@app.route('/choice/<user_number>')
def choice(user_number):
    server_number = int(session['server_number'])
    user_number = int(user_number)
    guess_status = verify_guess(user_number, server_number)
    guess_iter = 5
    if guess_status == 0:
        #message = f"Congratulation, you guessed {user_number} in {guess_iter+1} guesses"
        message = f"Congratulation, you guessed {user_number} Correctly"
        guessed = True
        
    if guess_status < 0:
        message = f"Try Again! You guessed too small"
    if guess_status > 0:
        message = f"Try Again! You guessed too high"
    json_msg = {"msg": message, "num": user_number}
        
    return jsonify(json_msg)


def verify_guess(user_number, server_number):
    if user_number == server_number:
        return 0
    
    if user_number > server_number:
        return 1
    
    if user_number < server_number:
        return -1
    pass
if __name__ == '__main__':
   app.run()