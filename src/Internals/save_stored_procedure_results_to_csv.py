import os

def save_stored_procedure_results_to_csv(df, file_name):
    """Guarda el DataFrame en un archivo CSV, reemplazando si ya existe."""

    # Crear la carpeta si no existe
    directory = 'src/input'
    os.makedirs(directory, exist_ok=True)

    # Crear la ruta completa del archivo
    file_path = os.path.join(directory, f"{file_name}.csv")

    # Si el archivo ya existe, eliminarlo (opcional, por claridad)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Archivo existente eliminado: {file_path}")

    # Guardar el nuevo archivo CSV
    df.to_csv(file_path, index=False)
    print(f"Nuevo archivo guardado en: {file_path}")
