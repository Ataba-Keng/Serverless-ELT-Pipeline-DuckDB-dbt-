# 🦆 Serverless ELT Pipeline (DuckDB + dbt)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-Core-FF694B?style=flat&logo=dbt&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-In--Process-FFF000?style=flat&logo=duckdb&logoColor=black)

Ce projet est une démonstration d'une **Modern Data Stack ultra-légère (Serverless)**. 
Il implémente un pipeline ELT complet (Extract, Load, Transform) sans nécessiter d'infrastructure lourde (pas de Docker, pas de serveur Postgres), grâce à la puissance de **DuckDB**.

## 🏗 Architecture

Contrairement aux stacks classiques (Airbyte/Postgres/Airflow) qui consomment beaucoup de RAM, cette architecture "Single Node" traite les données directement en processus local :

1.  **Ingestion (Python) :** Génération et chargement de données brutes (Mock Data) vers DuckDB.
2.  **Storage (DuckDB) :** Base de données OLAP embarquée (fichier local).
3.  **Transformation (dbt) :** Nettoyage et modélisation des données via SQL modulaire.
4.  **Orchestration (Python) :** Un script pipeline gère les dépendances et l'exécution séquentielle.

## 🛠 Tech Stack

* **Ingestion :** Python (`pandas`, `faker`)
* **Data Warehouse :** DuckDB
* **Transformation :** dbt (data build tool) - adapter `dbt-duckdb`
* **Orchestration :** Script Python natif

## 🚀 Installation & Démarrage

### 1. Cloner le projet
```bash
git clone [https://github.com/ton-pseudo/lightweight-data-pipeline.git](https://github.com/ton-pseudo/lightweight-data-pipeline.git)
cd lightweight-data-pipeline
```
### 2. Configurer l'environnement
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Lancer le Pipeline
Le script pipeline.py exécute tout le flux (Ingestion -> dbt -> Tests) :
```bash
python pipeline.py
```
### 4. (Optionnel) Explorer les données

Pour voir le résultat des transformations sans ouvrir d'outil externe :
```bash

python check_data.py
```
📂 Structure du Projet
Plaintext
```
.
├── dbt_project/            # Projet dbt (Modèles SQL, config)
│   ├── models/             # Logique métier (Transformation)
│   └── dbt_project.yml     # Configuration dbt
├── ingest.py               # Script d'ingestion (Extract & Load)
├── pipeline.py             # Orchestrateur (Main Entrypoint)
├── check_data.py           # Script de vérification/Visualisation
├── profiles.yml            # Configuration de connexion DuckDB
└── requirements.txt        # Dépendances Python
```
📝 Auteur

Projet réalisé par keng ATABA dans le cadre d'un portfolio Data Engineering. Objectif : Démonstration d'optimisation de ressources et maîtrise de la Modern Data Stack.
