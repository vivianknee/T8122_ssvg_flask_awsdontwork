import sqlite3

cars = [
    (1, "ice", "truck", 10000),
    (2, "electric", "suv", 50000)
]

def create_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_car_table(cur, conn):
    cur.execute("""CREATE TABLE IF NOT EXISTS cars(
    carid INT PRIMARY KEY,
    engine TEXT,
    type TEXT,
    price INT);
    """)
    conn.commit()

def insert_car_data(cars, cur, conn):
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?, ?);", cars)
    conn.commit()

def init_db():
    print("hello world")
    conn = create_db("car.db")

    cur = conn.cursor()

    create_car_table(cur, conn)

    insert_car_data(cars, cur, conn)

if __name__ == "__main__":
    init_db()

