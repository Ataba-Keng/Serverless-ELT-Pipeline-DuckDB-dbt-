import duckdb
import pandas as pd
from faker import Faker

DB_NAME = "ecommerce.duckdb"
fake = Faker()

def generate_users(n=100):
    users = []
    for _ in range(n):
        users.append({
            "id": _ +1,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country(),
            "created_at": fake.date_time_this_decade()
        })
    return pd.DataFrame(users)

def main():
    print("Gneretation des données")
    df_users = generate_users(500)

    con = duckdb.connect(DB_NAME)
    con.execute("CREATE OR REPLACE TABLE raw_users AS SELECT * FROM df_users")
    print(f"500 utilisateurs chargés dans {DB_NAME} (Table: raw_users)")

    count = con.execute("SELECT COUNT(*) FROM raw_users").fetchone()[0]
    print(f"total lignes : {count}")

    con.close()

if __name__ == "__main__" :
        main()