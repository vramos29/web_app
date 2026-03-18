from flask import Flask, abort, render_template, redirect, request, url_for

import main


from_main = main

#Flask operations
app = Flask(__name__)


#main route once server starts
@app.route('/')
def home():  
    return '<h1>This is the weather report app starter page</h1>'

#Fetches live weather, saves it, returns record
@app.route('/ingest?city=city&country=country', methods = ['POST'])
def enter_request():
    return '<h1>This is where you can generate a weather report</h1>'

#Retrieves all stored observations
@app.route('/observations', methods = ['GET'])
def retrieve_report():
    return '<h1>This is where you can read ALL the weather report(s)</h1>'

#Retrieves a specific obervation by ID
@app.route('/observations/<int:id>', methods = ['GET'])
def update_report(id):
    return f'<h1>This allows you to view a certain weather report: {id} </h1>'

#Updates a previously made observation
@app.route('/observations/<int:id>', methods = ['PUT'])
def update_report(id):
    return f'<h1>This allows you to update a certain weather report: {id} </h1>'

#Deletes an observation from the Database
@app.route('/observations/<int:id>', methods = ['DELETE'])
def update_report(id):
    return f'<h1>This allows you to delete a certain weather report: {id} </h1>'

"""
#This will allow you to download a copy of the report(s)
@app.route('/download-report')
def download_report():
    return '<h1>This will allow you to download a copy of the report</h1>'
"""

# This ensures the server only runs if the script is executed directly - returns TypeError.
if __name__ == '__main__':
    app.run(debug=True)

