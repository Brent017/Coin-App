import psycopg2
conn = psycopg2.connect("host=localhost dbname=coins")
cur = conn.cursor()
with open('q.csv', 'r') as f:
	cur.copy_from(f, 'coindb', sep=',')
	conn.commit()