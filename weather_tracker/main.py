import requests
import response as r
import patterns as rp
from flask import Flask, request, render_template
from datetime import datetime


#Flask operations
app = Flask(__name__)


#main route once server starts, takes user input
@app.route('/', methods=['GET', 'POST'])
def home():

    print(request.method)
    if request.method == "POST":
        
        city = request.form.get("city").strip().capitalize()
        country = request.form.get("country").strip().title()
        if not city or not country:
            return render_template('dashboard.html', error="Please enter the correct values")
        
        geo_data = r.geo_request(city, country)
        if "error" in geo_data:
            return render_template("dashboard.html", geo=geo_data)
        
        meteo_data = r.meteo_request(geo_data["latitude"], geo_data["longitude"])
        if "error" in meteo_data:
            return render_template("dashboard.html", meteo=meteo_data)
        
        report = r.report_form(geo_data, meteo_data)
        print(report)
        
        return render_template('dashboard.html', report=report)


    return render_template('dashboard.html')

#put main start into a function, call it from / route, then pass variables in it to be run

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

