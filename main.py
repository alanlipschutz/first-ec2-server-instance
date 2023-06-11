from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, this is my first server running in a ec2 instance!'


if __name__ == '__main__':
    app.run()
