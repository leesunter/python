from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('main.html', name=name)
if __name__ == '__main__':
    app.run()
    
# You can open a browser and go to http://127.0.0.1:5000/