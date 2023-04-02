import sqlite3

def read_file():
    global data
    data = []
    with open('input.txt', 'r') as file:
        for line in file:   
            data.append(line.split(', '))
    print(data)

def create_table():
    global db, cursor
    db = sqlite3.connect('cars.db')
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars_info (
            id INTEGER UNIQUE,
            make TEXT,
            model TEXT,
            age INTEGER,
            milleage INTEGER,
            owner TEXT
        ); 
    """)
    db.commit()

def insert_data():
    for line in data:
        cursor.execute("""
            INSERT INTO cars_info VALUES (?, ?, ?, ?, ?, ?);
        """, line) 
    db.commit()   

def update_data():
    cursor.execute("""
        UPDATE cars_info SET owner='Pasha' WHERE id=1;
    """)    
    db.commit()



read_file()
create_table()
# insert_data()
update_data()