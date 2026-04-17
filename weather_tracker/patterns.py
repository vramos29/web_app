import psycopg
import os
from dotenv import load_dotenv
from datetime import datetime




class DatabaseManager:
    """manages ORM operations"""

    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.connection_string=f"dbname={dbname} user={user} password={password} host={host} port={port}"
        print(self.connection_string)
    
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
            return self._insert()
            #inserts new object (INSERT)
        else:
            return self._update()
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

    def _insert(self):
        """Inserts a new report into the database"""
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                query = f"""
                    INSERT INTO {self.TABLE_NAME} (city, country, report_id, latitude, longitude, temp, elevation, windspeed, observation_time, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING city, country, windspeed, temp, observation_time
                """
                cur.execute(query, (self.id, self.city, self.country, self.latitude, self.longitude, self.temp, self.elevation, self.windspeed, self.observation, self.created))
                result = cur.fetchone()
                self.id = result[0]
                self.created = result[1]
                conn.commit()
                return self
            
    def _update(self):
        """Updates an existing report in the database"""
        with self.db.get_connection() as conn:
            with conn.cursor as cur:
                query = f"""
                    UPDATE {self.TABLE_NAME}
                    SET windspeed = %s, temp %s
                    WHERE report_id = %s
                """
                cur.execute(query, (self.windspeed, self.temp, self.id))
                conn.commit()
                return self
            
    def delete(self):
        """Deletes a report from the database"""
        if self.id is None:
            return False
        
        with self.db.get_connection() as conn:
            with conn.cursor() as cur:
                query = f"DELETE FROM {self.TABLE_NAME} WHERE report_id = %s"
                cur.execute(query, (self.id,))
                conn.commit()
                self.id = None #shows it is deleted and can be replaced
                return True
    
    @classmethod
    def find(cls, db_manager, report_id):
        """Finds a report by ID"""
        with db_manager.get_connection() as conn:
            with conn.cursor() as cur:
                query = f"SELECT report_id, city, country, windspeed, temp, observation_time FROM {cls.TABLE_NAME} WHERE report_id = %s"
                cur.execute(query, (report_id,))
                result = cur.fetchone()

                if result:
                    return Report(db_manager,
                                  city=result[1],
                                  country=result[2],
                                  report_id=result[0],
                                  temp=result[3],
                                  windspeed=result[4],
                                  observation_time=result[5])
                return None
            
    
    @classmethod
    def all(cls, db_manager):
        """Get every report from the database"""
        with db_manager.get_connection() as conn:
            with conn.cursor() as cur:
                query = f"SELECT report_id, city, country, windspeed, temp, observation_time FROM {cls.TABLE_NAME} ORDER BY report_id"
                cur.execute(query)
                results = cur.fetchall()

                reports = []
                for row in results:
                    reports.append(Report(db_manager,
                                          city=row[1],
                                          country=row[2],
                                          report_id=row[0],
                                          windspeed=row[3],
                                          temp=row[4],
                                          observation_time=row[5]))
                return reports
            
    def __repr__(self):
        return f"<Report(id={self.id}, city='{self.city}', country='{self.country}', temperature='{self.temp}', windspeed='{self.windspeed}')"
    

load_dotenv()  # Loads variables from .env file

username = os.getenv('db_user')
password = os.getenv('db_pass')
dbname = os.getenv('dbname')

db = DatabaseManager(dbname, username, password)

#Create a new record
"""
new_record = Report(db, 11, 'Johnson City', 'US', 30.27687, -98.41197, 23.3, 367.0, 24.8, '2026-04-16T16:15', '2026-04-16 11:31:45.41727')
new_record.save()
print(f"Create report: {new_record}")
"""

