import psycopg
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # Loads variables from .env file

username = os.getenv('db_user')
password = os.getenv('db_pass')
dbname = os.getenv('dbname')


#print(username) #works, successfully retrieves user and pass from .env file
#print(password)
#print(dbname)

#start here, you got this


"""
class Report:
    "maps to Reports table"
    def __init__(self, city, country, report_id=None, latitude=None, longitude=None, temp=None, elevation=None, windspeed=None, observation_time=None, created_at=None):
        self.id = report_id
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temp = temp
        self.elevation = elevation
        self.windspeed = windspeed
        self.observation_time = observation_time
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"<Report(report_id={self.id}, city='{self.city}', country='{self.country}')>"
    

report = Report("Chicago", "US")

print(report)

"""

class DatabaseManager:
    """manages ORM operations"""

    def __init__(self, dbname=dbname, user=username, password=password, host="localhost", port=5432):
        self.connection_string = f"dbname={dbname} user={user} password={password} host={host} port={port}"
    
    def get_connection(self):
        """Get database connection"""
        return psycopg.connect(self.connection_string)

class BaseModel:
    """Base class that all the other children models will inherit from"""

    TABLE_NAME = ""

    def __init__(self, db_manager):
        self.db = db_manager #for inheritence, possibly change this to 'from DatabaseManager' or something like that
    
    def save(self):
        """Saves current instance to DB"""
        if self.id is None:
            return self.insert()
            #inserts new object (INSERT)
        else:
            return self.update()
            #updates existing object (UPDATE)
    
    def _insert(self):
        """Inserts new report"""
        raise NotImplementedError("Subclasses MUST implement _insert")
    
    def _update(self):
        """Updates existing report"""
        raise NotImplementedError("Subclasses MUST implement _update")
    
    def delete(self):
        """Deletes current instance of report object"""
        raise NotImplementedError("Subclasses MUST implement delete")
    
    @classmethod
    def find(cls, db_manager, id):
        """Finds a report by its ID"""
        raise NotImplementedError("Subclasses MUST implement find")
    
#Above is the skeleton, below is the implementation

class Report(BaseModel):
    """Report model that maps to weatherreport table"""

    TABLE_NAME = "weatherreport"

    def __init__(self, db_manager, city, country, report_id, latitude, longitude, temp, elevation, windspeed, observation_time, created_at):
        super().__init__(db_manager)
        self.id = report_id
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temp = temp
        self.elevation = elevation
        self.windspeed = windspeed
        self.observation = observation_time
        self.created = created_at or datetime.now()

    