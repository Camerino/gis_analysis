import psycopg2

connection = psycopg2.connect("dbname=spatial port=5432 user=alim password=120507 host=localhost")
cursor.execute("SELECT name FROM geodata.bikeways WHERE type='Local Street'"
for row in cursor:
    print row[0],row[1]