import sqlite3
import licence_plate

def database_values(plate_detail):
    conn = sqlite3.connect('licencePlate.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS violatordetails(data text)''')
    plate_number = str(plate_detail)
    print("Inside Database"+plate_number)
    c.execute("INSERT INTO violatordetails VALUES(?)",(plate_number,))
    conn.commit()
    conn.close()
    return "Success"


def display():
    conn = sqlite3.connect('licencePlate.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM violatordetails'):
        print(row)

