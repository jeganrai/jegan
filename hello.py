from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!kjhkjhhkj'
@app.route('/about')
def hello_world():
    return 'Hello about'

if __name__ == '__main__':
    app.run()
