from flask import Flask, abort, render_template, redirect, request, url_for

import main


from_main = main

#Flask operations
app = Flask(__name__)


#main route once server starts
@app.route('/')
def home():  
    return '<h1>This is the weather report app starter page</h1>'


#This will be the post route that allows the user to enter the location for the weather report
@app.route('/main')
def enter_request():
    return None

#After entering their request, this is the get route that will display the information requested
@app.route('/report')
def retrieve_report():
    return None

#This route will allow the user to first view their reports, then update OR delete a report that has already been recorded and stored
@app.route('/report-update')
def update_report():
    return None


# This ensures the server only runs if the script is executed directly - returns TypeError.
if __name__ == '__main__':
    app.run(debug=True)

