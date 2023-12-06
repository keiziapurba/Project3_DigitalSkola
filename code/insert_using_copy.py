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
            CREATE TABLE IF NOT EXISTS user_using_copy_project3_keizia(
                id serial primary key,
                email text,
                name text,
                phone text,
                postal_code text
            )
            """)

with open ("/Users/keiziapurba/Desktop/Digital_Skola_DE/Project_3/source/users_w_postal_code.csv", "r") as f :
    next(f)
    cur.copy_from(f, "user_using_copy_project3_keizia", sep=",", columns=("email", "name", "phone", "postal_code"))

conn.commit()