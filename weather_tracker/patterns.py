import psycopg

class DbManager:

    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.connection_string = f"dbname={dbname} user={user} password={password} host={host} port={port}"
    
    def get_connection(self):
        return psycopg.connect(self.connection_string)
    
class Model:
    TABLE_NAME = ""

    def __init__(self, db_manager):
        self.db = db_manager

    def save(self):
        if self.id is None:
            return self._insert()   #Inserts new object
        else:
            return self.update()    #Updates existing object
        
    def _insert(self):
        raise NotImplementedError("Subclasses must implement _insert")
    
    def _update(self):
        """Update an existing record"""
        raise NotImplementedError("Subclasses must implement _update")
    
    def delete(self):
        """Delete the current instance from the database"""
        raise NotImplementedError("Subclasses must implement delete")
    
    @classmethod
    def find(cls, db_manager, id):
        """Find a record by ID"""
        raise NotImplementedError("Subclasses must implement find")
    

class Report(Model):

    TABLE_NAME = "weatherreport"

    def __init__(self, db_manager, report_id=None, city=str, country=str, latitude=float, longitude=float, temp=float, elevation=float, windspeed=float, observation_time=str):
        super().__init__(db_manager)
        self.id = report_id
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temp = temp
        self.elevation = elevation
        self.windspeed = windspeed
        self.observation_time = observation_time

    def _insert(self):
        with self.db.get_connection() as con:
            with con.cursor() as cur:
                query = f"""
                    INSERT INTO {self.TABLE_NAME} (city, country, latitude, longitude, temp, elevation, windspeed, observation_time)
                    VALES (%s, %s, %s)
                    RETURNING report_id, observation_time
                """
                cur.execute(query, (self.city, self.country, self.observation_time))
                result = cur.fetchone()
                self.id = result[0]
                self.observation_time = result[1]
                con.commit()
                return self
    
    def _update(self):
        with self.db.get_connection() as con:
            with con.cursor() as cur:
                query = f"""
                    UPDATE {self.TABLE_NAME}
                    SET temp = %s, windspeed = %s
                    WHERE report_id = %s
                """
                cur.execute(query, (self.temp, self.windspeed, self.id))
                con.commit()
                return self
    
    def delete(self):
        if self.id is None:
            return False
        
        with self.db.get_connection() as con:
            with con.cursor() as cur:
                query = f"""DELETE FROM {self.TABLE_NAME} WHERE report_id = %s"""
                cur.execute(query, (self.id))
                con.commit()
                self.id = None
                return True
            
    @classmethod
    def find(cls, db_manager, report_id):
        with db_manager.get_connection as con:
            with con.cursor() as cur:
                query = f"""SELECT report_id, city, country, temp, windspeed, observation_time FROM {cls.TABLE_NAME} WHERE user_id = %s"""
                cur.execute(query, (report_id))
                result = cur.fetchone()

                if result:
                    return Report(db_manager,
                                  report_id=result[0],
                                  city=result[1],
                                  country=result[2],
                                  temp=result[3],
                                  windspeed=result[4],
                                  observation_time=result[5])
                return None

    @classmethod       
    def all(cls, db_manager):
        with db_manager.get_connection() as con:
            with con.cursor as cur:
                query = f"""SELECT report_id, city, country, temp, windspeed, observation_time FROM {cls.TABLE_NAME} ORDER BY user_id"""
                cur.execute(query)
                results = cur.fetchall()

                reports = []
                for row in results:
                    reports.append(Report(db_manager,
                                  report_id=row[1],
                                  city=row[2],
                                  country=row[3],
                                  temp=row[4],
                                  windspeed=row[5],
                                  observation_time=row[6]))
                    return reports
                
    def __repr__(self):
        return f"<Report(id={self.id}), city='{self.city}', country='{self.country}', observation_time='{self.observation_time}')>"
