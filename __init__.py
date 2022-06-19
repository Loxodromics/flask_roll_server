# import main Flask class and request object
from flask import Flask, request, jsonify
# import random number generator
import random

def nextRandomNumber(session, round, dice):
    random.seed(session * round)
    return random.randint(1, dice)

# create the Flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Rollserver!"

@app.route('/roll_html')
def query_example():
    # if key doesn't exist, returns None
    session = int(request.args.get('session'))
    round = int(request.args.get('round'))
    dice = int(request.args.get('d'))
    roll = nextRandomNumber(session, round, dice)

    return '''<h1>Roll Server</h1><h2>Result for Round: {}, Session: {}</h2><h3>Roll (D{}): {}</3>'''.format(round, session, dice, 
roll)

@app.route('/roll_json')
def json_example():
    # if key doesn't exist, returns None
    session = int(request.args.get('session'))
    round = int(request.args.get('round'))
    dice = int(request.args.get('d'))

    roll = nextRandomNumber(session, round, dice)
    answer = {'session': session, 'round': round, 'roll': roll, 'd': dice}
    return jsonify(answer)

if __name__ == "__main__":
    app.run()
