import sqlite3


conn = sqlite3.connect(":memory:")

with conn:
    cur = conn.cursor()
    cur.execute('DROP TABLE if exists db_crew')
    cur.execute('CREATE TABLE db_crew (crew_name TEXT, crew_species TEXT, crew_iq INT);')
    cur.execute('INSERT INTO db_crew VALUES ("Jean-Baptiste Zorg", "Human", 122), ("Korben Dallas", "Meat Popsicle", 100), ("Ak\'not", "Mangalore", -5);')
    cur.execute('UPDATE db_crew SET crew_species = "Human" WHERE crew_name = "Korben Dallas";')
    cur.execute('SELECT * FROM db_crew WHERE crew_species = "Human"')
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row)
    conn.commit()
conn.close()
    
