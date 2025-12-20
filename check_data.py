import duckdb

# Connexion à la base
con = duckdb.connect("ecommerce.duckdb")

# 1. Voir toutes les tables disponibles
print(" Tables dans la base :")
tables = con.execute("SHOW TABLES").fetchall()
for table in tables:
    print(f"- {table[0]}")

print("-" * 30)

# 2. Lire le résultat de dbt (la table transformée)
# Dbt crée souvent les tables dans un schéma 'main' par défaut sur DuckDB
print(" Top 5 des pays (Table customers_per_country) :")
try:
    # Attention : dbt utilise le nom du fichier .sql comme nom de table/vue
    df = con.execute("SELECT * FROM customers_per_country LIMIT 5").df()
    print(df)
except Exception as e:
    print(f"Erreur : {e}")
    print("Essayons avec le nom complet si besoin...")
    # Parfois dbt met ça dans main.customers_per_country ou autre

con.close()