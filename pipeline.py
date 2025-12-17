import os
import time

def run_command(step_name, command):
    print(f"\n l[ETAPE] {step_name}...")
    start_time = time.time()
    exit_code = os.system(command)

    duration = round(time.time() - start_time, 2)

    if exit_code == 0 :
    
        print(f"{step_name} terminé en {duration}s")
    else:
        print(f"Échec de l'étape {step_name} !")
        exit(1)

if __name__ == "__main__" :
    print(" DÉMARRAGE DU PIPELINE DATA")
    run_command("ingestion (Extract & Load)", "python ingest.py")
    run_command("Transformation (dbt)", "cd dbt_project && dbt run")
    run_command("Contrôle Qualité", "python check_data.py")
    print("\n Pipeline terminé avec succès !")
    