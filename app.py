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
@app.route('/weather', methods = ['POST'])
def enter_request():
    return '<h1>This is where you can generate a weather report</h1>'

#After entering their request, this is the get route that will display the information requested
@app.route('/weather-report', methods = ['GET'])
def retrieve_report():
    return '<h1>This is where you can read ALL the weather report(s)</h1>'

#This route will allow the user to first view their reports, then update OR delete a report that has already been recorded and stored
@app.route('/update-report/<int:id>', methods = ['GET', 'PUT'])
def update_report(id):
    return f'<h1>This allows you to view then update a certain weather report: {id} </h1>'

@app.route('/update-report', methods = ['GET', 'DELETE'])
def delete_report(id):
    return f'<h1>and this allows you to view then delete a certain weather report as desired {id}</h1>'

#This will allow you to download a copy of the report(s)
@app.route('/download-report')
def download_report():
    return '<h1>This will allow you to download a copy of the report</h1>'

# This ensures the server only runs if the script is executed directly - returns TypeError.
if __name__ == '__main__':
    app.run(debug=True)

