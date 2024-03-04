#flask file to make login system secure
from flask import Flask, render_template
#type 'python3 -m pip install flask' or 'pip install flask' to get flask installed

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mainpage.html')
