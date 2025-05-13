import os
from datetime import datetime

def save_stored_procedure_results_to_csv(df, file_name):
    """Guarda el DataFrame en un archivo CSV con la fecha y hora actual."""
    # Crear la carpeta si no existe
    os.makedirs('src/input/', exist_ok=True)

    # Crear el nombre del archivo
    file_path = f'src/input/{file_name}.csv'

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(file_path, index=False)
    print(f"Archivo guardado en: {file_path}")