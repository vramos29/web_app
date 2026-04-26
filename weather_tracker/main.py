import requests
import response as r
import patterns as d
from flask import Flask, request, render_template, redirect, url_for
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
        # ^ properly retireves full weather report object

        

        new_record = d.Report(
            db_manager=d.db,
            report_id=None,
            city=report.city,
            country=report.country,
            latitude=report.latitude,
            longitude=report.longitude,
            temp=report.temp,
            elevation=report.elevation,
            windspeed=report.windspeed,
            observation_time=report.observation_time,
            created_at=None
        )

        new_record.save()
        return redirect(url_for('show_reports'))


    return render_template('dashboard.html')


#Fetches live weather, saves it, returns record
@app.route('/observations', methods = ['GET'])
def show_reports():
    reports = d.Report.all(d.db)
    return render_template('observations.html', reports=reports)


#Retrieves a specific obervation by ID
@app.route('/edit_observations/<int:id>', methods = ['GET'])
def edit_report(id):
    report = d.Report.find(d.db, id)
    return render_template('edit_observations.html', report=report)


#Reroutes to a edit page, where all values listed below can be edited
@app.route('/edit_observations/<int:id>', methods=["POST"])
def update_report(id):
    report = d.Report.find(d.db, id)
    report.city = request.form['city']
    report.country = request.form['country']
    report.latitude = float_values(request.form['latitude'])
    report.longitude = float_values(request.form['longitude'])
    report.temp = float_values(request.form['temp'])
    report.elevation = float_values(request.form['elevation'])
    report.windspeed = float_values(request.form['windspeed'])
    report.observation_time = (request.form['observation_time'])

    report._update()

    return redirect(url_for('show_reports'))


#Deletes an observation from the Database
@app.route('/edit_observations/<int:id>/delete', methods = ['GET'])
def delete_report(id):
    report = d.Report.find(d.db, id)
    report.delete()
    return redirect(url_for('show_reports'))


#allows float values to be properly transferred back into sql database without "None" str
def float_values(values):
    if values in ("", "None", None):
        return None
    return float(values)



# This ensures the server only runs if the script is executed directly - returns TypeError.
if __name__ == '__main__':
    app.run(debug=True)

