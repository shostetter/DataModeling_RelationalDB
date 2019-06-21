# Sparify Song Activity Data Pipeline  

## Purpose#
The data pipeline reads the Sparkify song and log files and inserts in the sparkify database. The database structure is optimized to facilitate analytics team queries on users and the songs they are listening to.  The pipeline generates a star database schema, containing 5 tables (1 fact table and 4 dimension tables). 

## Running data pipeline  
If running for the first time, where no database or tables exists, run the *create_tables.py* file. The create_tables script will create the sparkify database. **CAUTION:** This will drop any existing database named sparkify, so only run if no such database exists in the environment.  

To add new log file and/or song data to the existing tables in sparkify database, only the *etl.py* script is needed.  The *etl.py* script will parse any json files in the song_data and log_data sub directories of the data directory. The data in the json files will be added to the existing tables in the sparkify database.  
  
#### Upserts
In most cases the pipeline will do nothing on conflicts with primary keys. There are two exceptions to this, in the *user* and *artist* tables. In the user table on conflict with the user ID, the user's level and name will be updated. This was done to allow for users to modify their level and for name changes. In the artist table on conflict the location is updated, to allow for situations where an artist moves.  
 
#### Testing data pipeline
There is an additional *QA.ipynb* Jupyter Notebook that can be run to verify that the counts in the log files match the counts in the database. This notebook also contains some sample queries exploring the data. 

## Database schema    
The star schema design will enable faster read performance and simple query structures.   
For example, to explore the gender breakdown of the Sparkify users:  
`SELECT gender, COUNT(DISTINCT user_id) as cnt  
    FROM users   
    GROUP BY gender`  
or to explore the distribution of sessions per user:  
`SELECT user_id, COUNT(DISTINCT session_id)    
FROM songplays   
GROUP BY user_id`  

## Database Tables
1. **Fact Table**
    1. songplays (log data associated with song plays)  
     - songplay_id 
     - start_time 
     - user_id 
     - level 
     - song_id 
     - artist_id
     - session_id
     - location
     - user_agent  
 
1. **Dimension Tables**
    1. users 
     - user_id
     - first_name
     - last_name
     - gender
     - level
    1. songs 
     - song_id
     - title
     - artist_id
     - year
     - duration
    1. artists
     - artist_id
     - name
     - location
     - lattitude
     - longitude
    1. time (timstamps of log data)
     - start_time
     - hour
     - day
     - week
     - month
     - year
     - weekday  
  