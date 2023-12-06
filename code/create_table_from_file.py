import pandas as pd
from sqlalchemy  import create_engine


host = "pg-dev-dev-101.a.aivencloud.com"
port = "16506"
dbname = "defaultdb"
user = "avnadmin"
password = "AVNS_WKCKGD4JC5s0lel9zKD"


df = pd.read_csv("/Users/keiziapurba/Desktop/Digital_Skola_DE/Project_3/source/users_w_postal_code.csv")

engine = create_engine("postgresql://avnadmin:AVNS_WKCKGD4JC5s0lel9zKD@pg-dev-dev-101.a.aivencloud.com:16506/defaultdb")


df.to_sql("users_w_postal_code", engine)