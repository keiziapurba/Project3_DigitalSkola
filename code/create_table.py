import psycopg2


host = "pg-dev-dev-101.a.aivencloud.com"
port = "16506"
dbname = "defaultdb"
user = "avnadmin"
password = "AVNS_WKCKGD4JC5s0lel9zKD"

conn =  psycopg2.connect(("host={host} dbname={dbname} user={user} password={password} port={port}").format(host=host,dbname=dbname,user=user,password=password,port=port))

cur = conn.cursor()

# Create table

cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan_project3_keizia(
                id serial primary key,
                email text,
                name text,
                phone text,
                postal_code text
            )
            """)

conn.commit()

# print("Table berhasil dibuat")