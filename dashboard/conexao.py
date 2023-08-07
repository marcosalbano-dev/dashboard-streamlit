import psycopg2

conn = psycopg2.connect(dbname='sige', user='postgres', password='Axp@01fal12', port='5432', host='localhost')
cursor = conn.cursor()

if cursor:
    print('Conexão OK!')

# cursor.close()
# conn.close()