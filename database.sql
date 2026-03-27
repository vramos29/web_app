CREATE TABLE weatherreport (
    report_id SERIAL PRIMARY KEY,
    city VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(100) UNIQUE NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    temp FLOAT,
    elevation FLOAT,
    windspeed FLOAT,
    observation_time VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
)

SELECT * FROM weatherreport
SELECT * FROM weatherreport WHERE report_id=1