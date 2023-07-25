from flask import Flask, render_template, request, jsonify
import random, requests
from forms import RandomFactForm
from flask_wtf import FlaskForm

app = Flask(__name__)

BASE_URL = 'http://numbersapi.com'

colors = ("red","green","orange","blue")

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=['POST'])

def get_lucky_num():
    """API endpoint to get lucky num fact"""

    name = request.json['name']
    email = request.json['email']
    birth_year = request.json['birth_year']
    color = request.json['color']
    submission = {'name':name,'email':email, 'birth_year': birth_year, 'color': color}
    
    
    form = RandomFactForm(obj=submission,meta={'csrf':False})


   
    if form.validate_on_submit():

        random_number = random.randint(1,100)

        number_res = requests.get(f'{BASE_URL}/{random_number}')
        year_res = requests.get(f'{BASE_URL}/{birth_year}/year')

        number_text = number_res.text
        year_text = year_res.text

        num = {"fact":number_text,
            "num":random_number}
        
        year = {"fact":year_text,
                "num":birth_year}

        return jsonify(num=num, year=year)

    return jsonify(errors=form.errors)




        # errors = {}

        # if not name:
        #     errors['name'] = ['This field is required']

        # if color and color not in colors:
        #     errors['colors'] = ['Invalid color. must be one of: red, green, orange, blue']

        # if errors:
        #     return jsonify(errors=errors)