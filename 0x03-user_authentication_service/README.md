0x03. User authentication service

Declaring API Routes in a Flask App:
Flask is a micro web framework for Python. Defining API routes involves mapping URL paths to specific functions in your Flask application.
To declare a route, you typically use a decorator like @app.route('/path'), where app is your Flask application instance, and /path is the URL path you want to map.
Here's a basic example:
python
Copy code
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
Getting and Setting Cookies:
Cookies are small pieces of data sent from a website and stored on the user's computer by the user's web browser.
In Flask, you can get and set cookies using the request and response objects.
To set a cookie, you can use response.set_cookie('name', 'value').
To get a cookie, you can use request.cookies.get('name').
Example:
python
Copy code
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('Setting cookie')
    resp.set_cookie('username', 'john')
    return resp

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Cookie Value: {username}'

if __name__ == '__main__':
    app.run(debug=True)
Retrieving Request Form Data:
In Flask, you can access form data sent by a client using the request object.
If the request method is POST, you can use request.form['key'] to access form data.
Example:
python
Copy code
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # Do something with the data
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)
Returning Various HTTP Status Codes:
Flask allows you to return HTTP status codes along with your response using the status parameter in the return statement.
Example:
python

from flask import Flask

app = Flask(__name__)

@app.route('/not-found')
def not_found():
    return 'Page Not Found', 404

if __name__ == '__main__':
    app.run(debug=True)
