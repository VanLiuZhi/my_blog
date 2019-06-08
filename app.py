from flask import Blueprint, render_template, Flask
# main = Blueprint('main', __name__, template_folder='public')

# @main.route('/')
# def index():
#     return render_template('index.html')

app = Flask(__name__, template_folder='public')
# app.register_blueprint(main, url_prefix='/main')

@app.route('/learn_programing')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()