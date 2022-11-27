from flask import Flask
from flask import request

application = Flask(__name__)


@application.route("/")
def hello():
    name = request.args.get('name')
    message = request.args.get('message')
    main = f'Hello {name}! {message}!'
    return main


if __name__ == '__main__':
    application.run(host='0.0.0.0')



