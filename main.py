from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("https://raytorin.github.io/for_rekruto/", methods=['GET'])
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'Hello {name}! {message}!'


if __name__ == '__main__':
    app.run()


