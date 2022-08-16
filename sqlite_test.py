import sqlite3

peopleValues = (("Ron", "Obvious", 42), ("Luigi", "Vercotti", 43), ("Arthur", "Belling", 28))

with sqlite3.connect('test_db.db') as conn:
    cur = conn.cursor()
    cur.execute('SELECT FirstName, LastName FROM People WHERE Age > 30')
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row)
            
