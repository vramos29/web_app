-- Active: 1774581904917@@127.0.0.1@5432@Web App DB
CREATE TABLE weatherreport (
    report_id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    temp FLOAT,
    elevation FLOAT,
    windspeed FLOAT,
    observation_time VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

SELECT * FROM weatherreport;
SELECT * FROM weatherreport WHERE report_id=1;

DROP TABLE weatherreport;

INSERT into weatherreport(city, country, latitude, longitude, temp, elevation, windspeed, observation_time) VALUES
('Chicago', 'US', 41.85003, -87.65005, 0.4, 178.0, 4.1, '2026-03-28T02:30'),
('Dallas', 'US', 32.78306, -96.80667, 12.7, 140.0, 18.5, '2026-03-28T02:45'),
('Nashville', 'US', 36.16589, -86.78444, 7.6, 158.0, 17.7, '2026-03-28T02:45'),
('Knoxville', 'US', 35.96064, -83.92074, 9.2, 276.0, 17.3, '2026-03-28T02:45'),
('Boston', 'US', 42.35843, -71.05977, -0.4, 19.0, 10.2, '2026-03-28T02:45'),
('Portland', 'US', 45.52345, -122.67621, 13.9, 13.0, 12.1, '2026-03-28T02:45'),
('Birmingham', 'GB', 52.48142, -1.89983, 4.1, 151.0, 14.4, '2026-03-28T02:45'),
('Atlanta', 'US', 33.749, -84.38798, 17.8, 327.0, 23.4, '2026-03-28T02:45'),
('Detroit', 'US', 42.33143, -83.04575, -0.8, 182.0, 5.1, '2026-03-28T02:45'),
('Memphis', 'US', 35.14953, -90.04898, 8.7, 84.0, 17.4, '2026-03-28T02:45');


ALTER DATABASE "Web App DB" RENAME TO Web_App_DB;