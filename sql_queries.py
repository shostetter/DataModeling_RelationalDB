# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songplays"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp,
    user_id int,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int,
    location varchar,
    user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE users (
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
)
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id varchar PRIMARY KEY, 
    title varchar,
    artist_id varchar, 
    year int, 
    duration numeric
    )
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id TEXT PRIMARY KEY,
    artist_name TEXT,
    artist_location TEXT,
    artist_latitude double precision,
    artist_longitude double precision    
)
""")

time_table_create = ("""
CREATE TABLE time (
    start_time timestamp PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int,
    year int,
    weekday varchar
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(
    start_time,
    user_id,
    level,
    song_id,
    artist_id, 
    session_id, 
    location,
    user_agent
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)

""")

user_table_insert = ("""
INSERT INTO users (
    user_id,
    first_name, 
    last_name, 
    gender, 
    level
    ) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE 
        SET level = EXCLUDED.level,
        first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name
""")

song_table_insert = ("""
    INSERT INTO songs 
    (
        song_id, 
        title, 
        artist_id, 
        year, 
        duration
    ) VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""    
INSERT INTO artists 
(
    artist_id,
    artist_name,
    artist_location,
    artist_latitude,
    artist_longitude
) VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO UPDATE
    SET artist_location = EXCLUDED.artist_location,
    artist_latitude = EXCLUDED.artist_latitude,
    artist_longitude = EXCLUDED.artist_longitude    
""")


time_table_insert = ("""
INSERT INTO time 
(
    start_time,
    hour,
    day,  
    week, 
    month,
    year,
    weekday
    ) VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, s.artist_id 
FROM songs s
JOIN artists a
	ON s.artist_id=a.artist_id 
WHERE title = %s
	AND a.artist_name = %s 
	AND duration = %s;
    """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]