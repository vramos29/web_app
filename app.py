from flask import Flask, abort, render_template, redirect, request, url_for

import main


#Flask operations
app = Flask(__name__)


@app.route('/')
def home():  
    return '<h1>This is the weather report app starter page</h1>'

# This ensures the server only runs if the script is executed directly - returns TypeError.
if __name__ == '__main__':
    app.run(debug=True)

