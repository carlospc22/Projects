# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"

user_table_drop = "DROP TABLE IF EXISTS usuarios;"

song_table_drop = "DROP TABLE IF EXISTS musicas;"

artist_table_drop = "DROP TABLE IF EXISTS artistas;"

time_table_drop = "DROP TABLE IF EXISTS tempo;"




# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time BIGINT,
        user_id INT,
        nivel VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INT,
        localizacao VARCHAR,
        user_agent VARCHAR
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS usuarios (
        user_id INT PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        genero VARCHAR,
        nivel VARCHAR
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS musicas (
        song_id VARCHAR NOT NULL PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        artist_id VARCHAR(255) NOT NULL,
        ano INT,
        duracao FLOAT);
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artistas (
        artist_id VARCHAR(255) NOT NULL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        localizacao VARCHAR,
        latitude FLOAT,
        longitude FLOAT);
""")



time_table_create = ("""
    CREATE TABLE IF NOT EXISTS tempo (
        start_time BIGINT PRIMARY KEY,
        hora INT,
        dia INT,
        semana INT,
        mes INT,
        ano INT,
        dia_da_semana INT
    );
""")






# INSERT RECORDS
songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id, nivel, song_id,
                           artist_id, session_id, localizacao, user_agent)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO usuarios (user_id, first_name, last_name, genero, nivel)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO musicas (song_id, titulo, artist_id, ano, duracao)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artistas (artist_id, nome, localizacao, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO tempo (start_time, hora, dia, semana, mes, ano, dia_da_semana)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id
    FROM songs s
    JOIN artists a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create,
                        time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
