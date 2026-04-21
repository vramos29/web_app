from patterns import Report as report
from main import WeatherReport as data
from flask import Flask, render_template
from datetime import datetime

#Flask operations
app = Flask(__name__)


#main route once server starts
@app.route('/')
def home():  
    return render_template('dashboard.html')

"""
#Fetches live weather, saves it, returns record
@app.route('/ingest?city=city&country=country', methods = ['POST'])
def enter_request():
    result = report._insert(data)
    return render_template()

#Retrieves all stored observations
@app.route('/observations', methods = ['GET'])
def retrieve_report():
    result = report.all(data)
    return render_template()

#Retrieves a specific obervation by ID
@app.route('/observations/<int:id>', methods = ['GET'])
def update_report(id):
    result = report.find(data)
    return render_template()

#Updates a previously made observation
@app.route('/observations/<int:id>', methods = ['PUT'])
def update_report(id):
    result = report._update(data)
    return render_template()

#Deletes an observation from the Database
@app.route('/observations/<int:id>', methods = ['DELETE'])
def update_report(id):
    result = report.delete(data)
    return render_template()



"""
# This ensures the server only runs if the script is executed directly - returns TypeError.
if __name__ == '__main__':
    app.run(debug=True)

