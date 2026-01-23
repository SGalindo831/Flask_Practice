from flask import Flask, render_template
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)