from flask import Flask
from flask import render_template
from .dashboard.dash_app import init_keeper,init_defender

app = Flask(__name__,instance_relative_config=False)
app.config.from_object('config.Config')

@app.route('/')
def home():
    return render_template(
        'index.html'
    )

@app.route('/defender')
def defender(app):
    app = init_defender(app)

@app.route('/keeper')
def keeper(app):
    app = init_keeper(app)


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5555,debug=True)